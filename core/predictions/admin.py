from django.contrib import admin
from core.predictions.models import (
    PresupuestoServicios,
    PresupuestoDetallesServicios,
    Servicios,
    PublicacionesFacebook,
)

admin.site.register(PresupuestoServicios)
admin.site.register(PresupuestoDetallesServicios)
admin.site.register(Servicios)
admin.site.register(PublicacionesFacebook)
