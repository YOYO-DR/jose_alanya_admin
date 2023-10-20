from django.db import models


class PresupuestoServicios(models.Model):
    id_presupuesto_servicio = models.AutoField(primary_key=True)
    codigo_servicio = models.CharField(max_length=20)
    fecha_servicio = models.DateField()
    fecha_caducidad_servicio = models.DateField()
    tipo_descuento_servicio = models.CharField(max_length=22)
    monto_descuento_servicio = models.DecimalField(max_digits=18, decimal_places=2)
    con_sin_igv_servicio = models.CharField(max_length=15)
    sub_total_servicio = models.DecimalField(max_digits=18, decimal_places=2)
    total_impuesto_servicio = models.DecimalField(
        max_digits=18, decimal_places=2, null=True
    )
    total_servicio = models.DecimalField(max_digits=18, decimal_places=2)
    estado_servicio = models.CharField(max_length=22)
    referencia_servicio = models.CharField(max_length=100, null=True)
    nota_admin_servicio = models.CharField(max_length=6000, null=True)
    nota_cliente_servicio = models.CharField(max_length=6000, null=True)
    terminos_condiciones_servicio = models.CharField(max_length=2000, null=True)
    tipo_monto_descuento = models.CharField(max_length=100, null=True)
    monto_descuento_oficial = models.DecimalField(
        max_digits=20, decimal_places=0, null=True
    )
    empleado_id = models.IntegerField()
    perfil_cliente_id = models.IntegerField()
    impuesto_id = models.IntegerField()
    moneda_id = models.IntegerField()
    sede_id = models.IntegerField(null=True)
    empresa_id = models.IntegerField(null=True)


class Servicios(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=250)
    descripcion_servicio = models.TextField(null=True)
    precio_servicio = models.DecimalField(max_digits=18, decimal_places=2)
    categoria_id = models.IntegerField()
    unidad_medida_id = models.IntegerField()
    activo_servicio = models.IntegerField()
    empresa_id = models.IntegerField()
    sede_id = models.IntegerField()



class PresupuestoDetallesServicios(models.Model):
    id_presupuesto_detalle_servicio = models.AutoField(primary_key=True)
    titulo_presup_det_ser = models.CharField(max_length=100)
    cantidad_presup_det_ser = models.IntegerField()
    precio_venta_presup_det_ser = models.DecimalField(max_digits=18, decimal_places=2)
    importe_venta_presup_det_ser = models.DecimalField(max_digits=18, decimal_places=2)

    presupuesto_servicio = models.ForeignKey(
        PresupuestoServicios, on_delete=models.CASCADE
    )
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)



class PublicacionesFacebook(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    Tipo_publicacion = models.TextField()
    Descripcion_publicacion = models.TextField(null=True)
    imagen_publicacion = models.TextField(null=True)
    servicio_referencia = models.TextField(null=True)
    comentarios = models.IntegerField(default=0)
    fecha_publicacion = models.DateField(null=True)
    hora_publicacion = models.TimeField(null=True)

