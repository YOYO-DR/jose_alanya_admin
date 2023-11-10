from datetime import datetime, date, timedelta
from django.db.models import Sum, Count, Q, F
from django.views.generic import ListView, TemplateView
from django.db.models import Count

from django.http import JsonResponse

from random import randint

from core.predictions.models import (
    PresupuestoServicios,
    Servicios,
    PredictedData,
    PredictedDataTensorFlowModel,
    PredictedDataForPublicacionesFacebook,
    PredictedDataProphetResumen,
    PredictedProphetLandingModel,
    PredictedLandingResumen,
)


data_determinada = date(2023, 11, 15)  # Substitua essa data pela data desejada


class ChartView(ListView):
    template_name = "predictions/table.html"
    model = Servicios
    chart_title = None
    page_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chart_title"] = self.chart_title
        context["qs"] = self.object_list
        context["page_url"] = self.page_url
        context["dynamic_colors"] = [
            f"rgb({randint(0, 255)},{randint(0, 255)},{randint(0, 255)})"
            for _ in self.object_list
        ]
        return context

    @property
    def filters(self):
        limit = self.request.GET.get("limit", None)
        filter_date = self.request.GET.get("date", None)
        return {
            "date": datetime.strptime( filter_date, "%Y-%m-%d").date() if filter_date else str(date.today()),
            "limit": int(limit) if limit else 10,
            "ordenate": self.request.GET.get("ordenate", "-count"),
        }


class ChartByQuantityView(ChartView):
    chart_title = "Servicios por cantidad"
    page_url = "by-quantity"

    def get_queryset(self):
        presupuestos_filtrados = PresupuestoServicios.objects.filter(
            fecha_servicio__lt=self.filters["date"]
        )
        return (
            Servicios.objects.filter(
                presupuestodetallesservicios__presupuesto_servicio__in=presupuestos_filtrados
            )
            .values("nombre_servicio")
            .annotate(
                count=Count("id_servicio")
            )
            .order_by(self.filters["ordenate"])[0:self.filters["limit"]]
        )


class ChartByValueView(ChartView):
    chart_title = "Servicios por valor"
    page_url = "by-value"

    def get_queryset(self):
        presupuestos_filtrados = PresupuestoServicios.objects.filter(
            fecha_servicio__lt=self.filters["date"]
        )

        return (
            Servicios.objects.filter(
                presupuestodetallesservicios__presupuesto_servicio__in=presupuestos_filtrados
            )
            .values("nombre_servicio")
            .annotate(
                count=Sum("precio_servicio")
            )
            .order_by(self.filters["ordenate"])[0:self.filters["limit"]]
        )

def transform_data(data):
    # transform data from Phophet
    final_data = []
    index = 1
    for i in data:
        final_data.append(
            {
                "id": i["id"],
                "index": index,
                "date": i["date_predict"].strftime("%Y-%m-%d"),
                "service_id": i["service_id"],
                "less_probable_low_id": i["less_probable_low_id"],
                "less_probable_high_id": i["less_probable_high_id"],
                "name_high": i["name_high"],
                "name_less_low": i["name_less_low"],
                "name_less_high": i["name_less_high"],
            }
        )
        # add a numeric index column
        index += 1

    return final_data

def get_predicted_data():
    # Prohepht
    data = list(PredictedData.objects
            .annotate(name_high=F('service__nombre_servicio'))
            .annotate(name_less_low=F('less_probable_low__nombre_servicio'))
            .annotate(name_less_high=F('less_probable_high__nombre_servicio'))
            .values(
                'id', 'date_predict', 'service_id',  'less_probable_low_id',
                'less_probable_high_id', 'name_high', 'name_less_low', 'name_less_high')
            .order_by('-id')
    )
    return data


class PredictionView(ListView):
    """Show days of prediction using Prophet"""
    template_name = 'predictions/predictions_list.html'
    model = PredictedData

    def get_context_data(self, *, object_list=[], **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['qs'] = list(PredictedData.objects.order_by('-date_predict'))[-7:]
        context['chart_title'] = 'Predicted Data'
        context["dynamic_colors"] = [
            f"rgb({randint(0, 255)},{randint(0, 255)},{randint(0, 255)})"
            for _ in [1, 2, 3]
        ]
        context['last_resumen'] = PredictedDataProphetResumen.objects.last()

        context['initial_date'] = date.today()
        context['initial_days'] = 7

        date_day = self.request.GET.get('date', None)
        days = self.request.GET.get('number_days', 7)

        if date_day:
            date_day = datetime.strptime(date_day, "%Y-%m-%d").date()


            context['initial_date'] = date_day
            context['initial_days'] = days

            all_dates = [date_day + timedelta(days=i) for i in range(int(days))]
            context['qs'] = list(PredictedData.objects.filter(date_predict__in=all_dates).order_by('date_predict'))

        context['title'] = f'Predicción Prophet - Probables Servicios Siguientes {days} dias'
        len_qs = len(context['qs'])

        if len_qs != int(days):
            context['title'] += f' (Solo hay {len_qs} de {days} dias)'

        # calculate services repetidos
        all_services = [q.service for q in context['qs']]
        k = {}
        for i in all_services:
            if i in k:
                k[i] += 1
            else:
                k[i] = 1
        all_data = []
        for i,j in k.items():
            all_data.append({'service': i.nombre_servicio, 'count': j})
        context['all_data'] = all_data

        context['cant_predicted'] = Servicios.objects.last().id_servicio
        context['cant_predicted_half'] = int(context['cant_predicted'])

        return context

    def post(self, request, *args, **kwargs):
        data={}
        try:
            # obtengo la accion de la peticion
            action=request.POST['action']
            if action =='searchdata':
                data = get_predicted_data()[-7:]
                data = transform_data(data)
            else:
                # si no se envia el action, retorno el error
                data['error'] ='No ha ingresado a ninguna opcion'
        except Exception as e:
            # si hay un error en el codigo, lo envio
            data={}
            data['error']=str (e)
        return JsonResponse(data, safe=False)


class PredictionViewThirty(ListView):
    """Show days of prediction using Tensorflow-Keras"""
    template_name = 'predictions/predictions_list_thirty.html'
    model = PredictedData

    def get_context_data(self, *, object_list=[], **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['qs'] = list(PredictedData.objects.order_by('-date_predict'))[-10:]
        context['chart_title'] = 'Predicted Data'
        context["dynamic_colors"] = [
            f"rgb({randint(0, 255)},{randint(0, 255)},{randint(0, 255)})"
            for _ in [1, 2, 3]
        ]
        context['title'] = 'Predicción Prophet - Probables Servicios Siguientes 30 dias'
        context['last_tensor'] = PredictedDataTensorFlowModel.objects.last()
        # context['last_resumen'] = PredictedDataProphetResumen.objects.last()
        return context

    def post(self, request, *args, **kwargs):
        data={}
        try:
            # obtengo la accion de la peticion
            action=request.POST['action']
            if action =='searchdata':
                data = get_predicted_data()[-30:]
                data = transform_data(data)
            else:
                # si no se envia el action, retorno el error
                data['error'] ='No ha ingresado a ninguna opcion'
        except Exception as e:
            # si hay un error en el codigo, lo envio
            data={}
            data['error']=str (e)
        return JsonResponse(data, safe=False)

class PredictionPublicationFacebookView(TemplateView):
    template_name = 'predictions/predictions_publications_facebook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Predicción Probable Servicio usando Publicaciones de Facebook'
        context['last_tensor'] = PredictedDataForPublicacionesFacebook.objects.last()
        context['last_resumen'] = PredictedDataProphetResumen.objects.last()
        return context


class PredictionLandingPageView(TemplateView):
    template_name = 'predictions/predictions_landing.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Prediciones usando Landing Page'
        context['predicted'] = PredictedProphetLandingModel.objects.last()
        context['resumen'] = PredictedLandingResumen.objects.last()

        context['initial_date'] = date.today()
        date_fecha = self.request.GET.get('date', None)


        if date_fecha:
            # transform from iso format to date
            date_fecha = datetime.strptime(date_fecha, "%Y-%m-%d").date()

            context['initial_date'] = date_fecha

            p = PredictedLandingResumen.objects.filter(date_predict=date_fecha).first()
            if p:
                list_most, list_clicks = p.get_list_landing_most()
            else:
                list_most, list_clicks = [], []
            context['list_landing_most'] = list_most

            # sumarize clicks for pages
            cliks_by_page = {}
            for i in list_clicks:
                if i['page'] in cliks_by_page:
                    cliks_by_page[i['page']] += 1
                else:
                    cliks_by_page[i['page']] = 1
            context['clicks_by_page'] = [{'page':i, 'click': v} for i,v in cliks_by_page.items()]
        return context


