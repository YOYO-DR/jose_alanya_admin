from django.db.models.functions import Cast
from datetime import datetime, date
import calendar

from django.db.models import Sum, Count, CharField
from django.db.models.functions import Coalesce
from django.db.models import FloatField
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView
from django.db.models import Count, Value
from datetime import datetime

from random import randint

from core.predictions.models import PresupuestoServicios, Servicios

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
