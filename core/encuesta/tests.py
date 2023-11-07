from django.test import TestCase
from core.encuesta.models import Pregunta
# Create your tests here.

preguntas_local=Pregunta.objects.using('default').all()
for pregunta in preguntas_local:
  Pregunta.objects.using('production').create(pregunta=pregunta.pregunta)
