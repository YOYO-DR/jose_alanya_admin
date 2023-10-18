from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.crm.forms import TrabajadorForm
from core.crm.mixins import ValidatePermissionRequiredMixin
from core.crm.models import Trabajador
from django.db.models import Q


class TrabajadorListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Trabajador
    template_name = 'trabajador/list.html'
    permission_required = 'crm.view_trabajador'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                if request.user.groups.filter(Q(name="administrador")).exists():
                    trabajadores=Trabajador.objects.all()
                elif request.user.groups.filter(Q(name="empresa")).exists():
                    trabajadores=Trabajador.objects.filter(sede__empresa=request.user.empresa)
                #permiso sede
                else:
                    trabajadores=Trabajador.objects.filter(sede=request.user.sede)
                for i in trabajadores:
                    data.append(i.toJSON())
            else:
                data={}
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Trabajadores'
        context['create_url'] = reverse_lazy('crm:trabajador_create')
        context['list_url'] = reverse_lazy('crm:trabajador_list')
        context['entity'] = 'Trabajadores'
        return context


class TrabajadorCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajador/create.html'
    success_url = reverse_lazy('crm:trabajador_list')
    permission_required = 'crm.add_trabajador'
    url_redirect = success_url

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación un Trabajador'
        context['entity'] = 'Trabajadores'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class TrabajadorUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajador/create.html'
    success_url = reverse_lazy('crm:trabajador_list')
    permission_required = 'crm.change_trabajador'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(Q(name="administrador")).exists():
          # empresa
          if request.user.groups.filter(Q(name="empresa")).exists():
            self.object=get_object_or_404(Trabajador,id=self.get_object().id,sede__empresa=request.user.empresa)
            #sede
          else:
            self.object=get_object_or_404(Trabajador,id=self.get_object().id,sede=request.user.sede)
        
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición un Trabajador'
        context['entity'] = 'Trabajadores'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class TrabajadorDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Trabajador
    template_name = 'trabajador/delete.html'
    success_url = reverse_lazy('crm:trabajador_list')
    permission_required = 'crm.delete_trabajador'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(Q(name="administrador")).exists():
          # empresa
          if request.user.groups.filter(Q(name="empresa")).exists():
            self.object=get_object_or_404(Trabajador,id=self.get_object().id,sede__empresa=request.user.empresa)
            #sede
          else:
            self.object=get_object_or_404(Trabajador,id=self.get_object().id,sede=request.user.sede)
        
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Trabajador'
        context['entity'] = 'Trabajadores'
        context['list_url'] = self.success_url
        return context