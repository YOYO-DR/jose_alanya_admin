from collections.abc import Iterable
from django.db import models
from django.forms import model_to_dict

# Create your models here.
class Pregunta(models.Model):
  pregunta=models.CharField(max_length=100,null=False,blank=False)

  def __str__(self):
    return self.pregunta
  
  def toJSON(self):
    return model_to_dict(self)

# respuestas
respuestas=(
  ('1','Nunca'),
  ('2','Casi nunca'),
  ('3','A veces'),
  ('4','Casi siempre'),
  ('5','Siempre'),
)
class Respuesta(models.Model):
  respuesta=models.CharField(max_length=10, choices=respuestas, default='1')
  pregunta=models.ForeignKey(Pregunta,on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.pregunta.pregunta} - {self.get_respuesta_display()}'