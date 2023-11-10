from django.contrib import admin
from core.predictions.models import (
    PresupuestoServicios,
    PresupuestoDetallesServicios,
    Servicios,
    PublicacionesFacebook,
    PredictedData,
    PredictedDataTensorFlowModel,
    PredictedDataForPublicacionesFacebook,
    PredictedDataProphetResumen,
    LandingPageUsuarios,
    PredictedProphetLandingModel,
    PredictedLandingResumen,
)

admin.site.register(PresupuestoServicios)


@admin.register(PublicacionesFacebook)
class PublicacionesFacebookAdmin(admin.ModelAdmin):
    list_display = ('id_publicacion', 'Tipo_publicacion', 'Descripcion_publicacion', 'imagen_publicacion', 'servicio_referencia', 'comentarios', 'fecha_publicacion', 'hora_publicacion')

@admin.register(PresupuestoDetallesServicios)
class PresupuestoDetallesServiciosAdmin(admin.ModelAdmin):
    search_fields = ('servicio__pk',)
    list_display = ('id_presupuesto_detalle_servicio', 'titulo_presup_det_ser', 'cantidad_presup_det_ser', 'precio_venta_presup_det_ser', 'importe_venta_presup_det_ser', 'presupuesto_servicio', 'servicio', 'get_servicio')

    def get_servicio(self, obj):
        return obj.servicio.pk


@admin.register(Servicios)
class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('id_servicio', 'nombre_servicio')


@admin.register(PredictedData)
class PredictedDataAdmin(admin.ModelAdmin):
    list_display = ('date_predict', 'service', 'get_service', 'date')

    def get_service(self, obj):
        return obj.service.pk

@admin.register(PredictedDataTensorFlowModel)
class PredictedDataTensorFlowModelAdmin(admin.ModelAdmin):
    pass

@admin.register(PredictedDataForPublicacionesFacebook)
class PredictedDataForPublicacionesFacebookAdmin(admin.ModelAdmin):
    pass

@admin.register(PredictedDataProphetResumen)
class PredictedDataProphetResumenAdmin(admin.ModelAdmin):
    list_display = ('id', 'period_init', 'period_end')


@admin.register(LandingPageUsuarios)
class LandingPageUsuariosAdmin(admin.ModelAdmin):
    list_display = ('ID', 'FECHA_INGRESO', 'TOTAL_CLICKS')

@admin.register(PredictedProphetLandingModel)
class PredictedProphetLandingModelAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(PredictedLandingResumen)
class PredictedLandingResumenAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_predict')

