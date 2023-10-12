from django.db import models
from datetime import datetime
from core.erp.choices import gender_choices
from django.forms import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL
from core.models import BaseModel
from crum import get_current_user

class Category(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, null=True,blank=True,verbose_name='Descripción')

    #si se auto completa con visual, los campos deben quedar asi, no utilizando ":" sino los "=" (error mio que vi)
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # hasta si necesito algo del request, puedo obtenerlo aqui con crum, y su funcion get_current_request()
        user = get_current_user()
        #si el usuario no esta vacio
        if user is not None:
          #si existe un pk o id, significa que se esta creando el registro, de lo contrario, se esta actualizando el registro
          if not self.pk:
              self.user_creation=user
          else:
              self.user_updated=user
        super(Category, self).save()

        
    def __str__(self):
        return f'{self.name}'
    
    def toJSON(self):
      #podria crear el diccionario manual pero donde tenga muchos atributos seria mala practica, ya django tiene una funcion para ello
      #puedo pasarle un arreglo en el parametro exclude con el nombre de los campos que no quiera que se retornen
      # puedo excluir valores del diccionario que genera el model_to_dict 
      item = model_to_dict(self, exclude=['user_creation','user_updated'])
      return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Product(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Categoria')
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True,verbose_name='Imagen')
    stock=models.IntegerField(default=0, verbose_name='Stock')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2,verbose_name='Precio de venta')

    def toJSON(self):
        item = model_to_dict(self)
        item['full_name']='{} / {}'.format(self.name, self.cat.name)
        item['cat']={"id":self.cat.id,"name":self.cat.name}
        item['image']=self.get_image()
        item['pvp']=format(self.pvp, '.2f')
        return item

    def get_image(self):
        #si existe la imagen, o bueno, si se subio, le retorno la ruta que debe estar en media url, y le junto el self.image que es el nombre de la imagen
        if self.image:
            return f'{MEDIA_URL}{self.image}'
        #de lo contrario, le retorno una imagen como predeterminada que esta en mis static
        return f'{STATIC_URL}media/img/empty.png'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Client(BaseModel):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    date_birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names
    
    def get_fullname(self):
        return f"{self.names} {self.surnames}"

    def toJSON(self):
        item = model_to_dict(self)
        item['gender'] = {'id':self.gender,'name':self.get_gender_display()} 
        item['date_birthday'] = self.date_birthday.strftime('%Y-%m-%d')
        return item
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']
