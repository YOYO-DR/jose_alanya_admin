from django.contrib import admin

from core.encuesta.models import Pregunta, Respuesta

# Register your models here.
admin.site.register(Pregunta)
admin.site.register(Respuesta)
