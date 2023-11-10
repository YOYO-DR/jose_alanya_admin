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

    def __str__(self):
        return self.nombre_servicio


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


class PredictedData(models.Model):
    """Generated with Prophet"""
    date = models.DateTimeField(auto_now_add=True)
    date_predict = models.DateField()
    service = models.ForeignKey(Servicios, on_delete=models.CASCADE) # most probable
    less_probable_low = models.ForeignKey(
        Servicios, on_delete=models.CASCADE, related_name="predicteds_low"
    )
    less_probable_high = models.ForeignKey(
        Servicios, on_delete=models.CASCADE, related_name="predicteds_high"
    )

    def __str__(self):
        return f'{self.date} - {self.service.nombre_servicio}'

class PredictedDataProphetResumen(models.Model):
    period_init = models.DateField(blank=True, null=True)
    period_end = models.DateField(blank=True, null=True)
    result_image = models.ImageField(upload_to='predicted_images_resumen', blank=True, null=True)
    historic_image = models.ImageField(upload_to='predicted_images_resumen', blank=True, null=True)

    def __str__(self):
        return f'{self.period_init} - {self.period_end}'

class PredictedDataTensorFlowModel(models.Model):
    """Generated with Keras-TensorFlow"""
    services = models.ManyToManyField(Servicios)
    image_predicted_7_days = models.ImageField(upload_to='predicted_images', blank=True, null=True)
    image_validate_model = models.ImageField(upload_to='validated_images', blank=True, null=True)
    image_compare_results = models.ImageField(upload_to='compare_images', blank=True, null=True)

    def __str__(self):
        return f'{self.pk}'


class PredictedDataForPublicacionesFacebook(models.Model):
    servicio_referencia = models.CharField(max_length=100, blank=True, null=True)
    image_predicted_7_days = models.ImageField(upload_to='predicted_images_publicaciones', blank=True, null=True)
    image_validate_model = models.ImageField(upload_to='validated_images_publicaciones', blank=True, null=True)
    image_compare_results = models.ImageField(upload_to='compare_images_publicaciones', blank=True, null=True)
    publications = models.ManyToManyField(PublicacionesFacebook)

    def __str__(self):
        return f'{self.servicio_referencia}'


class LandingPageUsuarios(models.Model):
    ID = models.IntegerField(primary_key=True)
    INICIO = models.IntegerField(null=True, default=None)
    NOSOTROS = models.IntegerField(null=True, default=None)
    MONITOREO_PARTICULAS = models.IntegerField(null=True, default=None)
    MONITOREO_CORROSION = models.IntegerField(null=True, default=None)
    DETECCION_INCENDIOS = models.IntegerField(null=True, default=None)
    DETECCION_ASPIRACION = models.IntegerField(null=True, default=None)
    HIGIENIZACION = models.IntegerField(null=True, default=None)
    AGENTES_LIMPIOS = models.IntegerField(null=True, default=None)
    SEGURIDAD_SALUD = models.IntegerField(null=True, default=None)
    SALUD_OCUPA = models.IntegerField(null=True, default=None)
    MONIT_OCUP = models.IntegerField(null=True, default=None)
    MEDIO_AMBIENTE = models.IntegerField(null=True, default=None)
    MONITOREO_MODELAMIENTO = models.IntegerField(null=True, default=None)
    OUTSOURCING = models.IntegerField(null=True, default=None)
    CERTIFICACIONES = models.IntegerField(null=True, default=None)
    CONTACTO = models.IntegerField(null=True, default=None)
    FECHA_INGRESO = models.DateField(null=True, default=None)
    TOTAL_CLICKS = models.IntegerField(null=True, default=None)

    def __str__(self):
        return str(self.ID)

    def get_pages_click(self):
        PAGES = []
        
        if self.INICIO:
            PAGES.append({'page': 'Inicio', 'click': self.INICIO})
        if self.NOSOTROS:
            PAGES.append({'page': 'Nosotros', 'click': self.NOSOTROS})
        if self.MONITOREO_PARTICULAS:
            PAGES.append({'page': 'Monitoreo de Partículas', 'click': self.MONITOREO_PARTICULAS})
        if self.MONITOREO_CORROSION:
            PAGES.append({'page': 'Monitoreo de Corrosión', 'click': self.MONITOREO_CORROSION})
        if self.DETECCION_INCENDIOS:
            PAGES.append({'page': 'Detección de Incendios', 'click': self.DETECCION_INCENDIOS})
        if self.DETECCION_ASPIRACION:
            PAGES.append({'page': 'Detección de Aspiración', 'click': self.DETECCION_ASPIRACION})
        if self.HIGIENIZACION:
            PAGES.append({'page': 'Higienización', 'click': self.HIGIENIZACION})
        if self.AGENTES_LIMPIOS:
            PAGES.append({'page': 'Agentes Limpios', 'click': self.AGENTES_LIMPIOS})
        if self.SEGURIDAD_SALUD:
            PAGES.append({'page': 'Seguridad y Salud', 'click': self.SEGURIDAD_SALUD})
        if self.SALUD_OCUPA:
            PAGES.append({'page': 'Salud Ocupacional', 'click': self.SALUD_OCUPA})
        if self.MONIT_OCUP:
            PAGES.append({'page': 'Monitoreo Ocupacional', 'click': self.MONIT_OCUP})
        if self.MEDIO_AMBIENTE:
            PAGES.append({'page': 'Medio Ambiente', 'click': self.MEDIO_AMBIENTE})
        if self.MONITOREO_MODELAMIENTO:
            PAGES.append({'page': 'Monitoreo y Modelamiento', 'click': self.MONITOREO_MODELAMIENTO})
        if self.OUTSOURCING:
            PAGES.append({'page': 'Outsourcing', 'click': self.OUTSOURCING})
        if self.CERTIFICACIONES:
            PAGES.append({'page': 'Certificaciones', 'click': self.CERTIFICACIONES})
        if self.CONTACTO:
            PAGES.append({'page': 'Contacto', 'click': self.CONTACTO})
        
        # Create a list orderd by clicks only with page key
        pages_click = sorted(PAGES, key=lambda k: k['click'], reverse=True)
        pages = [page['page'] for page in pages_click]
        return pages, pages_click

# Each Days
class PredictedLandingResumen(models.Model):
    landing_most = models.ManyToManyField(LandingPageUsuarios, related_name='landing_most_predicted')
    landing_less_low = models.ManyToManyField(LandingPageUsuarios, related_name='landing_less_low_predicted')
    landing_less_high = models.ManyToManyField(LandingPageUsuarios, related_name='landing_less_high_predicted')
    date_predict = models.DateField()

    def __str__(self):
        return f'{self.pk}'

    def get_list_landing_most(self):
        all_pages = []
        all_clicks = []
        for landing in self.landing_most.all():
            pages, clicks = landing.get_pages_click()
            all_pages.extend(pages)
            all_clicks.extend(clicks)
        return set(all_pages), all_clicks


# All images one instance
class PredictedProphetLandingModel(models.Model):
    landing_page = models.ManyToManyField(LandingPageUsuarios)
    image_generated = models.ImageField(upload_to='predicted_images_landing', blank=True, null=True)
    image_feed_model = models.ImageField(upload_to='feed_images_landing', blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.pk}'

