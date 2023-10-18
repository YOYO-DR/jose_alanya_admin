from crum import get_current_user
from django.forms import *
from django.contrib.auth.models import Group
from core.crm.models import Sede
from core.user.models import User
from django.db.models import Q


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user=get_current_user()
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True
        if not user.groups.filter(name="administrador").exists():
            self.fields['sede'].queryset=Sede.objects.filter(empresa=user.empresa)
            self.fields.pop('groups')
            self.fields.pop('empresa')

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password', 'image',"empresa","sede",'groups'
        widgets = {
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Ingrese su correo',
                }
            ),
            'username': TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre se usuario',
                }
            ),
            'password': PasswordInput(render_value=True,
                attrs={
                    'placeholder': 'Ingrese su contraseña',
                }
            ),
            'groups':SelectMultiple(attrs={
                'class':'form-control select2',
                'style': 'width 100%',
                'multiple':'multiple'
            })
        }
        exclude = ['user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff']


    def save(self, commit=True):
        user_ac=get_current_user()
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd=self.cleaned_data['password']
                u= form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user=User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
                if not user_ac.groups.filter(name="empresa").exists():
                  u.groups.clear()
                  for g in self.cleaned_data['groups']:
                    u.groups.add(g)
                else:
                    u.groups.clear()
                    u.groups.add(Group.objects.get(name="sede"))
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data