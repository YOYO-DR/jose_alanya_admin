from django.urls import path
from core.crm.views.categoria.views import *
from core.crm.views.dashboard.views import *
from core.crm.views.empresa.views import EmpresaCreateView, EmpresaDeleteView, EmpresaListView, EmpresaUpdateView
from core.crm.views.presupuesto.views import PresupuestoCreateView, PresupuestoDeleteView, PresupuestoListView, PresupuestoUpdateView
from core.crm.views.producto.views import *
from core.crm.views.sede.views import SedeCreateView, SedeDeleteView, SedeListView, SedeUpdateView
from core.crm.views.servicio.views import ServicioCreateView, ServicioDeleteView, ServicioListView, ServicioUpdateView
from core.crm.views.trabajador.views import TrabajadorCreateView, TrabajadorDeleteView, TrabajadorListView, TrabajadorUpdateView

app_name = 'crm'

urlpatterns = [
    #Categoria
    path('categoria/list/', CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/add/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/update/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria/delete/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_delete'),

    # producto
    path('producto/list/', ProductoListView.as_view(), name='producto_list'),
    path('producto/add/', ProductoCreateView.as_view(), name='producto_create'),
    path('producto/update/<int:pk>/', ProductoUpdateView.as_view(), name='producto_update'),
    path('producto/delete/<int:pk>/', ProductoDeleteView.as_view(), name='producto_delete'),

    # empresa
    path('empresa/list/', EmpresaListView.as_view(), name='empresa_list'),
    path('empresa/add/', EmpresaCreateView.as_view(), name='empresa_create'),
    path('empresa/update/<int:pk>/', EmpresaUpdateView.as_view(), name='empresa_update'),
    path('empresa/delete/<int:pk>/', EmpresaDeleteView.as_view(), name='empresa_delete'),

    # sede
    path('sede/list/', SedeListView.as_view(), name='sede_list'),
    path('sede/add/', SedeCreateView.as_view(), name='sede_create'),
    path('sede/update/<int:pk>/', SedeUpdateView.as_view(), name='sede_update'),
    path('sede/delete/<int:pk>/', SedeDeleteView.as_view(), name='sede_delete'),

    # trabajador
    path('trabajador/list/', TrabajadorListView.as_view(), name='trabajador_list'),
    path('trabajador/add/', TrabajadorCreateView.as_view(), name='trabajador_create'),
    path('trabajador/update/<int:pk>/', TrabajadorUpdateView.as_view(), name='trabajador_update'),
    path('trabajador/delete/<int:pk>/', TrabajadorDeleteView.as_view(), name='trabajador_delete'),

    #servicio
    path('servicio/list/', ServicioListView.as_view(), name='servicio_list'),
    path('servicio/add/', ServicioCreateView.as_view(), name='servicio_create'),
    path('servicio/update/<int:pk>/', ServicioUpdateView.as_view(), name='servicio_update'),
    path('servicio/delete/<int:pk>/', ServicioDeleteView.as_view(), name='servicio_delete'),
    
    #presupuesto
    path('presupuesto/list/', PresupuestoListView.as_view(), name='presupuesto_list'),
    path('presupuesto/add/', PresupuestoCreateView.as_view(), name='presupuesto_create'),
    path('presupuesto/update/<int:pk>/', PresupuestoUpdateView.as_view(), name='presupuesto_update'),
    path('presupuesto/delete/<int:pk>/', PresupuestoDeleteView.as_view(), name='presupuesto_delete'),

    #Home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

]        