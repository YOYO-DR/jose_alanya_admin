import json
from django.shortcuts import get_object_or_404
from core.crm.models import *
from django.views.generic import *
from django.utils.decorators import *
from django.http import *
from django.views.decorators.csrf import *
from core.crm.forms import *
from django.urls import *
from django.contrib.auth.decorators import * 
from core.crm.mixins import ValidatePermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db import transaction

# El LoginRequiredMixin es para validar que este Logueado
# El ValidatePermissionRequiredMixin validar los permisos para entrar a la vista

class PresupuestoListView(LoginRequiredMixin,ValidatePermissionRequiredMixin,ListView):
    # este atributo es para ponerle el nombre al permiso de esta vista, para que cuando se cree un grupo de permisos
    permission_required='crm.view_presupuesto'
    model=Presupuesto
    template_name='presupuesto/list.html'

    # esta funcion es la que manipula las peticiones por el metodo "POST"
    def post(self, request, *args, **kwargs):
        data={}
        try:
            # obtengo la accion de la peticion
            action=request.POST['action']
            if action =='searchdata':
                # aqui retorno todas las presupuestos y les pongo su metodo toJSON para convertirlo en diccionario y se pueda serializar (convertir a JSON)
                data=[]
                if request.user.groups.filter(Q(name="administrador")).exists():
                  cate=Presupuesto.objects.all()
                else:
                  cate=Presupuesto.objects.filter(empresa=request.user.empresa)
                for i in cate:
                    data.append(i.toJSON())
            elif action=="search_detalle_servi":
                data=[]
                for i in DetallePresupuesto.objects.filter(presupuesto_id=request.POST.get("id")):
                    data.append(i.toJSON())
            else:
                # si no se envia el action, retorno el error
                data['error'] ='No ha ingresado a ninguna opcion'
        except Exception as e:
            # si hay un error en el codigo, lo envio
            data={}
            data['error']=str (e)
        return JsonResponse(data, safe=False)
    
    # esta funcion es para enviar valores al template
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Listado de presupuestos'
        # el reverse_lazy es para obtener alguna url por su nombre ("app:name_url"), y retorna la url completa (https://...)
        context['create_url']=reverse_lazy('crm:presupuesto_create')
        context['list_url']=reverse_lazy('crm:presupuesto_list')
        context['entity']='Presupuestos'
        return context

class PresupuestoCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model=Presupuesto
    form_class=PresupuestoForm
    template_name='presupuesto/create.html'
    success_url=reverse_lazy('crm:presupuesto_list')
    permission_required = 'crm.add_presupuesto'
    url_redirect = success_url

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action=="search_servi":
                data=[]
                ids_exclude=json.loads(request.POST['ids'])
                servicios=Servicio.objects.filter(nombre__icontains=request.POST['term'])
                for i in servicios.exclude(id__in=ids_exclude)[0:10]:
                    item=i.toJSON()
                    #item['value']=i.Nombre
                    item['text']=i.nombre
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    presupuestos=json.loads(request.POST['ventas'])

                    presupuesto=Presupuesto()
                    presupuesto.fecha_servicio=presupuestos['fecha_servicio']
                    presupuesto.fecha_caducidad_servicio=presupuestos['fecha_caducidad_servicio']
                    presupuesto.monto_descuento_servicio=float(presupuestos['monto_descuento_servicio'])

                    presupuesto.con_sin_igv_servicio=float(presupuestos['con_sin_igv_servicio'])
                    presupuesto.sub_total_servicio=float(presupuestos['sub_total_servicio'])
                    presupuesto.total_impuesto_servicio=float(presupuestos['total_impuesto_servicio'])
                    presupuesto.total_servicio=float(presupuestos['total_servicio'])
                    presupuesto.estado_servicio=presupuestos['estado_servicio']
                    presupuesto.nota_admin_servicio=presupuestos['nota_admin_servicio']
                    presupuesto.nota_cliente_servicio=presupuestos['nota_cliente_servicio']
                    presupuesto.terminos_condiciones_servicio=presupuestos['terminos_condiciones_servicio']
                    presupuesto.monto_descuento_oficial=float(presupuestos['monto_descuento_oficial'])
                    presupuesto.monto_descuento_oficial=float(presupuestos['monto_descuento_oficial'])
                    presupuesto.sede_id=presupuestos['sede']
                    presupuesto.empresa_id=presupuestos['empresa']
                    presupuesto.save()

                    for i in presupuestos['servicios']:
                        det=DetallePresupuesto()
                        det.presupuesto_id=presupuesto.id
                        det.servicio_id=i['id']
                        det.cantidad=int(i['cantidad'])
                        det.precio=float(i['precio'])
                        det.subtotal=float(i['subtotal'])
                        det.save()

            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error']=str (e)
        return JsonResponse(data)
    
    def get_detalles_producto(self):
        data = []
        try:
            for i in DetallePresupuesto.objects.filter(presupuesto_id=self.get_object().id):
                item = i.servicio.toJSON()
                item['cantidad'] = i.cantidad
                # pasarlos a flotantes porque los Decimal no se puede serializar
                item['precio']=float(item['precio'])
                item['subtotal']=float(i.subtotal)
                data.append(item)
        except:
            pass
        return data


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Creacion de presupuestos'
        context['entity']='Presupuestos'
        context['list_url']=self.success_url
        context['action']='add'
        context['det']=json.dumps(self.get_detalles_servicio())

        return context 

class PresupuestoUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model=Presupuesto
    form_class=PresupuestoForm
    template_name='presupuesto/create.html'
    success_url=reverse_lazy('crm:presupuesto_list')
    permission_required = 'crm.change_presupuesto'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(Q(name="administrador")).exists():
          self.object=get_object_or_404(Presupuesto,id=self.get_object().id,empresa=request.user.empresa)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action=="search_servi":
                data=[]
                ids_exclude=json.loads(request.POST['ids'])
                servicios=Servicio.objects.filter(nombre__icontains=request.POST['term'])
                for i in servicios.exclude(id__in=ids_exclude)[0:10]:
                    item=i.toJSON()
                    #item['value']=i.Nombre
                    item['text']=i.nombre
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    presupuestos=json.loads(request.POST['ventas'])

                    presupuesto=Presupuesto()
                    presupuesto.fecha_servicio=presupuestos['fecha_servicio']
                    presupuesto.fecha_caducidad_servicio=presupuestos['fecha_caducidad_servicio']
                    presupuesto.monto_descuento_servicio=float(presupuestos['monto_descuento_servicio'])

                    presupuesto.con_sin_igv_servicio=float(presupuestos['con_sin_igv_servicio'])
                    presupuesto.sub_total_servicio=float(presupuestos['sub_total_servicio'])
                    presupuesto.total_impuesto_servicio=float(presupuestos['total_impuesto_servicio'])
                    presupuesto.total_servicio=float(presupuestos['total_servicio'])
                    presupuesto.estado_servicio=presupuestos['estado_servicio']
                    presupuesto.nota_admin_servicio=presupuestos['nota_admin_servicio']
                    presupuesto.nota_cliente_servicio=presupuestos['nota_cliente_servicio']
                    presupuesto.terminos_condiciones_servicio=presupuestos['terminos_condiciones_servicio']
                    presupuesto.monto_descuento_oficial=float(presupuestos['monto_descuento_oficial'])
                    presupuesto.monto_descuento_oficial=float(presupuestos['monto_descuento_oficial'])
                    presupuesto.sede_id=presupuestos['sede']
                    presupuesto.empresa_id=presupuestos['empresa']
                    presupuesto.save()

                    for i in presupuestos['servicios']:
                        det=DetallePresupuesto()
                        det.presupuesto_id=presupuesto.id
                        det.servicio_id=i['id']
                        det.cantidad=int(i['cantidad'])
                        det.precio=float(i['precio'])
                        det.subtotal=float(i['subtotal'])
                        det.save()

            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error']=str (e)
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Edicion de presupuestos'
        context['entity']='Presupuestos'
        context['list_url']=self.success_url
        context['action']='edit'
        return context 

class PresupuestoDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model=Presupuesto
    template_name='presupuesto/delete.html'
    success_url=reverse_lazy('crm:presupuesto_list')
    permission_required = 'crm.delete_presupuesto'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(Q(name="administrador")).exists():
          self.object=get_object_or_404(Presupuesto,id=self.get_object().id,empresa=request.user.empresa)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            self.object.delete()
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de una presupuesto'
        context['entity'] = 'Presupuestos'
        context['list_url'] = self.success_url
        return context