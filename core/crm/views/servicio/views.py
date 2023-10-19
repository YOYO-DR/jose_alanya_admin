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

# El LoginRequiredMixin es para validar que este Logueado
# El ValidatePermissionRequiredMixin validar los permisos para entrar a la vista

class ServicioListView(LoginRequiredMixin,ValidatePermissionRequiredMixin,ListView):
    # este atributo es para ponerle el nombre al permiso de esta vista, para que cuando se cree un grupo de permisos
    permission_required='crm.view_servicio'
    model=Servicio
    template_name='servicio/list.html'

    # esta funcion es la que manipula las peticiones por el metodo "POST"
    def post(self, request, *args, **kwargs):
        data={}
        try:
            # obtengo la accion de la peticion
            action=request.POST['action']
            if action =='searchdata':
                # aqui retorno todas los servicios y les pongo su metodo toJSON para convertirlo en diccionario y se pueda serializar (convertir a JSON)
                data=[]
                if request.user.groups.filter(Q(name="administrador")).exists():
                  cate=Servicio.objects.all()
                else:
                  cate=Servicio.objects.filter(empresa=request.user.empresa)
                for i in cate:
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
        context['title']='Listado de servicios'
        # el reverse_lazy es para obtener alguna url por su nombre ("app:name_url"), y retorna la url completa (https://...)
        context['create_url']=reverse_lazy('crm:servicio_create')
        context['list_url']=reverse_lazy('crm:servicio_list')
        context['entity']='Servicios'
        return context

class ServicioCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model=Servicio
    form_class=ServicioForm
    template_name='servicio/create.html'
    success_url=reverse_lazy('crm:servicio_list')
    permission_required = 'crm.add_servicio'
    url_redirect = success_url

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action == 'add':
                form=self.get_form()
                data=form.save()
            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error']=str (e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Creacion de servicios'
        context['entity']='Servicios'
        context['list_url']=self.success_url
        context['action']='add'
        return context 

class ServicioUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model=Servicio
    form_class=ServicioForm
    template_name='servicio/create.html'
    success_url=reverse_lazy('crm:servicio_list')
    permission_required = 'crm.change_servicio'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(Q(name="administrador")).exists():
          self.object=get_object_or_404(Servicio,id=self.get_object().id,empresa=request.user.empresa)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action=request.POST['action']
            if action == 'edit':
                form=self.get_form()
                data=form.save()
            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data={}
            data['error']=str (e)

        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Edicion de un servicio'
        context['entity']='Servicios'
        context['list_url']=self.success_url
        context['action']='edit'
        return context 

class ServicioDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model=Servicio
    template_name='servicio/delete.html'
    success_url=reverse_lazy('crm:servicio_list')
    permission_required = 'crm.delete_servicio'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(Q(name="administrador")).exists():
          self.object=get_object_or_404(Servicio,id=self.get_object().id,empresa=request.user.empresa)
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
        context['title'] = 'Eliminacion de un Servicio'
        context['entity'] = 'Servicios'
        context['list_url'] = self.success_url
        return context