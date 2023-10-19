from core.user.models import User
from core.crm.models import Empresa,Categoria,Producto,Sede,Trabajador
from core.crm.tests import grupos

# superususario de prueba
superuser=User.objects.filter(is_superuser=True,is_active=True).first()

# crear 2 empresas
empresa_1=Empresa(nombre="Empresa_1")
empresa_1.save(user_test=superuser)
empresa_2=Empresa(nombre="Empresa_2")
empresa_2.save(user_test=superuser)

# crear usuarios
# crear 2 usuarios de empresas
user_empresa_1,create=User.objects.get_or_create(username="usuario_empresa_1",email="usuarioempresa1@gmail.com",empresa=empresa_1)
user_empresa_1.groups.add(grupos['empresa'])
user_empresa_1.set_password("admin.2003")
user_empresa_1.save()

user_empresa_2,create=User.objects.get_or_create(username="usuario_empresa_2",email="usuarioempresa2@gmail.com",empresa=empresa_2)
user_empresa_2.groups.add(grupos['empresa'])
user_empresa_2.set_password("admin.2003")
user_empresa_2.save()

# crear 4 categorias (2 para cada empresa)
cate_1_empresa_1=Categoria(nombre="Salsas",empresa=empresa_1)
cate_1_empresa_1.save(user_test=user_empresa_1)
cate_2_empresa_1=Categoria(nombre="Sopas",empresa=empresa_1)
cate_2_empresa_1.save(user_test=user_empresa_1)
cate_1_empresa_2=Categoria(nombre="Carnes",empresa=empresa_2)
cate_1_empresa_2.save(user_test=user_empresa_2)
cate_2_empresa_2=Categoria(nombre="Jugos",empresa=empresa_2)
cate_2_empresa_2.save(user_test=user_empresa_2)

# crear 8 producots (2 para cada categoria)
prod_1_empresa_1=Producto(nombre="Tomate",categoria=cate_1_empresa_1,stock=10,precio=1000)
prod_1_empresa_1.save(user_test=user_empresa_1)
prod_2_empresa_1=Producto(nombre="Mayonesa",categoria=cate_1_empresa_1,stock=10,precio=1000)
prod_2_empresa_1.save(user_test=user_empresa_1)
prod_3_empresa_1=Producto(nombre="Tortilla",categoria=cate_2_empresa_1,stock=10,precio=1000)
prod_3_empresa_1.save(user_test=user_empresa_1)
prod_4_empresa_1=Producto(nombre="Mariscos",categoria=cate_2_empresa_1,stock=10,precio=1000)
prod_4_empresa_1.save(user_test=user_empresa_1)
prod_1_empresa_2=Producto(nombre="Milanesa",categoria=cate_1_empresa_2,stock=10,precio=1000)
prod_1_empresa_2.save(user_test=user_empresa_2)
prod_2_empresa_2=Producto(nombre="Res",categoria=cate_1_empresa_2,stock=10,precio=1000)
prod_2_empresa_2.save(user_test=user_empresa_2)
prod_3_empresa_2=Producto(nombre="Mango",categoria=cate_2_empresa_2,stock=10,precio=1000)
prod_3_empresa_2.save(user_test=user_empresa_2)
prod_4_empresa_2=Producto(nombre="Tropical",categoria=cate_2_empresa_2,stock=10,precio=1000)
prod_4_empresa_2.save(user_test=user_empresa_2)

# crear 4 sedes (2 pasa cada empresa)
sede_1_empresa_1=Sede(nombre="Sede 1",empresa=empresa_1)
sede_1_empresa_1.save(user_test=user_empresa_1)
sede_2_empresa_1=Sede(nombre="Sede 2",empresa=empresa_1)
sede_2_empresa_1.save(user_test=user_empresa_1)
sede_1_empresa_2=Sede(nombre="Sede 1",empresa=empresa_2)
sede_1_empresa_2.save(user_test=user_empresa_2)
sede_2_empresa_2=Sede(nombre="Sede 2",empresa=empresa_2)
sede_2_empresa_2.save(user_test=user_empresa_2)

print("Usuarios sede")
#crear 4 usuarios de sedes (2 para cada sede)
user_sede_1_empresa_1,create=User.objects.get_or_create(username="usuario_sede_1_empresa_1",sede=sede_1_empresa_1,email="usuariosede1empresa1@gmail.com")
user_sede_1_empresa_1.groups.add(grupos['sede'])
user_sede_1_empresa_1.set_password("admin.2003")
user_sede_1_empresa_1.save()

user_sede_2_empresa_1,create=User.objects.get_or_create(username="usuario_sede_2_empresa_1",sede=sede_2_empresa_1,email="usuariosede2empresa1@gmail.com")
user_sede_2_empresa_1.groups.add(grupos['sede'])
user_sede_2_empresa_1.set_password("admin.2003")
user_sede_2_empresa_1.save()

user_sede_1_empresa_2,create=User.objects.get_or_create(username="usuario_sede_1_empresa_2",sede=sede_1_empresa_2,email="usuariosede1empresa2@gmail.com")
user_sede_1_empresa_2.groups.add(grupos['sede'])
user_sede_1_empresa_2.set_password("admin.2003")
user_sede_1_empresa_2.save()

user_sede_2_empresa_2,create=User.objects.get_or_create(username="usuario_sede_2_empresa_2",sede=sede_2_empresa_2,email="usuariosede2empresa2@gmail.com")
user_sede_2_empresa_2.groups.add(grupos['sede'])
user_sede_2_empresa_2.set_password("admin.2003")
user_sede_2_empresa_2.save()

# crear 4 trabajadores, 1 de cada sede
tra_1=Trabajador(nombres="trabajador 1",apellidos="ape",edad=20,direccion="casa",correo="tra1@gmail.com",curriculum_vitae="curriculum",sede=sede_1_empresa_1)
tra_1.save(user_test=user_sede_1_empresa_1)
tra_2=Trabajador(nombres="trabajador 2",apellidos="ape",edad=20,direccion="casa",correo="tra2@gmail.com",curriculum_vitae="curriculum",sede=sede_2_empresa_1)
tra_2.save(user_test=user_sede_2_empresa_1)
tra_3=Trabajador(nombres="trabajador 3",apellidos="ape",edad=20,direccion="casa",correo="tra3@gmail.com",curriculum_vitae="curriculum",sede=sede_1_empresa_2)
tra_3.save(user_test=user_sede_1_empresa_2)
tra_4=Trabajador(nombres="trabajador 4",apellidos="ape",edad=20,direccion="casa",correo="tra4@gmail.com",curriculum_vitae="curriculum",sede=sede_2_empresa_2)
tra_4.save(user_test=user_sede_2_empresa_2)