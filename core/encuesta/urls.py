from django.urls import path

from core.encuesta.views import EncuestaView

urlpatterns = [
    path("",EncuestaView.as_view(),name="encuesta")
]
