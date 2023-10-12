from django.contrib import admin
from core.erp.models import *

# Registrar los modelos en el admin para que aparezcan en el administrador de django
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Client)