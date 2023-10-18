# crear permisos
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group,Permission
#diccionario con los permisos y grupos
permisos={}
grupos={}
# permiso de la vista empresa
# Obtener el ContentType del modelo al que se asignarán permisos
ct_empresa = ContentType.objects.get(app_label='crm', model='Empresa')
# Obtener los permisos específicos
permssion_empresa = Permission.objects.filter(codename__contains='_empresa', content_type=ct_empresa)
permisos['empresa']=permssion_empresa

# permiso de la vista empresa
# Obtener el ContentType del modelo al que se asignarán permisos
ct_categoria = ContentType.objects.get(app_label='crm', model='Categoria')
# Obtener los permisos específicos
permssion_categoria = Permission.objects.filter(codename__contains='_categoria', content_type=ct_categoria)
permisos['categoria']=permssion_categoria

# permiso de la vista producto
# Obtener el ContentType del modelo al que se asignarán permisos
ct_producto = ContentType.objects.get(app_label='crm', model='Producto')
# Obtener los permisos específicos
permission_producto = Permission.objects.filter(codename__contains='_producto', content_type=ct_producto)
permisos['producto']=permission_producto

# permiso de la vista sede
# Obtener el ContentType del modelo al que se asignarán permisos
ct_sede = ContentType.objects.get(app_label='crm', model='Sede')
# Obtener los permisos específicos
permission_sede = Permission.objects.filter(codename__contains='_sede', content_type=ct_sede)
permisos['sede']=permission_sede

# permiso de la vista trabajador
# Obtener el ContentType del modelo al que se asignarán permisos
ct_trabajador = ContentType.objects.get(app_label='crm', model='Trabajador')
# Obtener los permisos específicos
permission_trabajador = Permission.objects.filter(codename__contains='_trabajador', content_type=ct_trabajador)
permisos['trabajador']=permission_trabajador

# permiso de la vista usuario
# Obtener el ContentType del modelo al que se asignarán permisos
ct_user = ContentType.objects.get(app_label='user', model='User')
# Obtener los permisos específicos
permission_user = Permission.objects.filter(codename__contains='_user', content_type=ct_user)
permisos['user']=permission_user

# crear grupo administrador (super usuario)
group_admin,create=Group.objects.get_or_create(name="administrador")
if not create:
  group_admin.permissions.clear()
group_admin.permissions.add(*[a for a in Permission.objects.all()])
grupos['administrador']=group_admin

# crear grupo empresa (admin de una empresa, sus categorias, sus productos, sus sedes, de los usuarios que administren las sedes y sus trabajadores)
group_empresa,create=Group.objects.get_or_create(name="empresa")
if not create:
  group_empresa.permissions.clear()
group_empresa.permissions.add(*[*list(permssion_categoria),*list(permission_producto),*list(permission_sede),*list(permission_trabajador),*list(permission_user)])
grupos['empresa']=group_empresa
  
# crear grupo sede (admin de los trabajadores)

group_sede,create=Group.objects.get_or_create(name="sede")
if not create:
  group_sede.permissions.clear()
group_sede.permissions.add(*list(permission_trabajador))
grupos['sede']=group_sede