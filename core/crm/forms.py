from typing import Any
from django.forms import ModelForm,TextInput, Textarea,NumberInput,EmailInput,CheckboxInput
from crum import get_current_user
from core.crm.models import Categoria, Producto, Sede, Servicio, Trabajador,Empresa
from django.db.models import Q

class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = get_current_user()
        # si el usuario no es un super usuario y tiene una empresa registrada, entonces le omito la empresa en la creacion de una empresa, pero de los contrario si es un super usuario, le dejo asignar la empresa a la categoria
        if user.empresa and not user.groups.filter(name__iexact="administrador").exists():
            # aqui le quito la empresa de los fields
            self.fields.pop('empresa')
        self.fields['nombre'].widget.attrs['autofocus']= True

    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'placeholder': 'Ingrese una descripción',
                    'rows':3,
                    'cols':3
                }
            )
        }
        exclude = ['user_creation', 'user_updated']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
  
class ProductoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user=get_current_user()
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
        if user.groups.filter(Q(name="empresa")).exists():
          self.fields['categoria'].queryset = Categoria.objects.filter(empresa=user.empresa)

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
        }
        exclude=['user_creation','user_updated']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class TrabajadorForm(ModelForm):
  def __init__(self, *args, **kwargs):
      user=get_current_user()
      super().__init__(*args, **kwargs)
      if user.groups.filter(Q(name="empresa")).exists():
          self.fields['sede'].queryset = Sede.objects.filter(empresa=user.empresa)
      elif user.groups.filter(Q(name="sede")).exists():
          self.fields.pop("sede")
      self.fields['nombres'].widget.attrs['autofocus']= True

  class Meta:
    model=Trabajador
    fields="__all__"
    widgets={
        "nombres":TextInput(attrs={
            "placeholder":"Ingrese los nombres"
        }),
        "apellidos":TextInput(attrs={
            "placeholder":"Ingrese los apellidos"
        }),
        "edad":NumberInput(attrs={
            "placeholder":"Ingrese la edad"
        }),
        "direccion":TextInput(attrs={
            "placeholder":"Ingrese la dirección"
        }),
        "correo":EmailInput(attrs={
            "placeholder":"Ingrese el correo electrónico"
        }),
        "curriculum_vitae":TextInput(attrs={
            "placeholder":"Ingrese el curriculum vitae"
        })
    }
    exclude=['user_creation','user_updated']

  def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class EmpresaForm(ModelForm):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['nombre'].widget.attrs['autofocus']= True

    class Meta:
        model=Empresa
        widgets={
            "nombre":TextInput(
                attrs={"placeholder":"Ingrese el nombre"}
            )
        }
        fields="__all__"
        exclude=['user_creation','user_updated']
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class SedeForm(ModelForm):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      user = get_current_user()
        # si el usuario no es un super usuario y tiene una empresa registrada, entonces le omito la empresa en la creacion de una empresa, pero de los contrario si es un super usuario, le dejo asignar la empresa a la categoria
      if user.empresa and not user.groups.filter(name__iexact="administrador").exists():
            # aqui le quito la empresa de los fields
            self.fields.pop('empresa')
      self.fields['nombre'].widget.attrs['autofocus']= True

    class Meta:
        model=Sede
        widgets={
            "nombre":TextInput(
                attrs={"placeholder":"Ingrese el nombre"}
            )
        }
        fields="__all__"
        exclude=['user_creation','user_updated']
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ServicioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user=get_current_user()
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
        if user.groups.filter(Q(name="empresa")).exists():
          self.fields.pop("empresa")
          self.fields['categoria'].queryset = Categoria.objects.filter(empresa=user.empresa)
          self.fields['sede'].queryset = Sede.objects.filter(empresa=user.empresa)

    class Meta:
        model = Servicio
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'descripcion': TextInput(
                attrs={
                    'placeholder': 'Ingrese una descripción',
                }
            )
        }
        exclude=['user_creation','user_updated']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
