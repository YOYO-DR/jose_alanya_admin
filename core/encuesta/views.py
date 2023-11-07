from typing import Any
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.views.generic import ListView

from core.encuesta.models import Pregunta, Respuesta

class EncuestaView(ListView):
  template_name="encuesta.html"
  model=Pregunta

  def get_queryset(self):
    num=1
    query=[pre.toJSON() for pre in Pregunta.objects.all()]
    for pregunta in query:
      pregunta['numero']=num
      num+=1
    return query

  def post(self,request,*args,**kwargs):
    data={}
    datos=request.POST
    for clave,valor in datos.items():
      Respuesta.objects.create(respuesta=valor[0],pregunta_id=int(clave))
    return JsonResponse(data)
