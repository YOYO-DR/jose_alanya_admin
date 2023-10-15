from django.urls import path
from core.crm.views.categoria.views import *
from core.crm.views.dashboard.views import *
from core.crm.views.producto.views import *

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

    # # empresa
    # path('empresa/list/', ProductListView.as_view(), name='empresa_list'),
    # path('empresa/add/', ProductCreateView.as_view(), name='empresa_create'),
    # path('empresa/update/<int:pk>/', ProductUpdateView.as_view(), name='empresa_update'),
    # path('empresa/delete/<int:pk>/', ProductDeleteView.as_view(), name='empresa_delete'),

    # # sede
    # path('sede/list/', ProductListView.as_view(), name='sede_list'),
    # path('sede/add/', ProductCreateView.as_view(), name='sede_create'),
    # path('sede/update/<int:pk>/', ProductUpdateView.as_view(), name='sede_update'),
    # path('sede/delete/<int:pk>/', ProductDeleteView.as_view(), name='sede_delete'),

    # # trabajador
    # path('trabajador/list/', ProductListView.as_view(), name='trabajador_list'),
    # path('trabajador/add/', ProductCreateView.as_view(), name='trabajador_create'),
    # path('trabajador/update/<int:pk>/', ProductUpdateView.as_view(), name='trabajador_update'),
    # path('trabajador/delete/<int:pk>/', ProductDeleteView.as_view(), name='trabajador_delete'),

    #Home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

]        