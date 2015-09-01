from django.forms import ModelForm
from cotizacion.models import Estado_Cotizacion, \
    Piso, Tiempo_Carga, Cotizacion, Vehiculo, \
    Vehiculo_Cotizacion, Cotizacion_direccion, \
    Cotizacion_trabajador, Cotizacion_Ambiente, \
    Cotizacion_Mueble, Cotizacion_Servicio, \
    Cotizacion_Material, Cotizacion_Contenido
from servicio.models import Material


class EstadoCotizacionForm(ModelForm):
    class Meta:
        model = Estado_Cotizacion
        fields = '__all__'
        labels = {
            'estado': ('Estado de cotización'),
        }


class PisoForm(ModelForm):
    class Meta:
        model = Piso
        fields = '__all__'
        labels = {
            'piso': ('Piso del ambiente'),
            'factor': ('N° de pisos adicionales a recorrer')
        }


class TiempoCargaForm(ModelForm):
    class Meta:
        model = Tiempo_Carga
        fields = '__all__'
        labels = {
            'tiempo_carga': ('Tiempo de carga'),
            'volumen_min': ('Volúmen menor en m3'),
            'volumen_max': ('Volúmen mayor en m3'),
            'nro_objeto_min': ('Cantidad menor'),
            'nro_objeto_max': ('Cantidad mayor'),
            'peso_min': ('Peso menor en Kgs'),
            'peso_max': ('Peso mayor en Kgs')
        }


class CotizacionForm(ModelForm):
    class Meta:
        model = Cotizacion
        fields = '__all__'


class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('cantidad_total', 'modelo',
            'tarifa_hora', 'tarifa_recorrido',
            'capacidad_volumen', 'capacidad_peso', 'cargo')
        labels = {
            'cantidad_total': ('Cantidad de vehículos'),
            'modelo': ('Modelo de vehículo'),
            'tarifa_hora': ('Tarifa por tiempo en $/h'),
            'tarifa_recorrido': ('Tarifa por recorrido en $/Km'),
            'capacidad_volumen': ('Capacidad del vehículo en m3'),
            'capacidad_peso': ('Capacidad del vehículo en Kgs'),
            'cargo': ('Conductor designado')
        }


class VehiculoCotizacionForm(ModelForm):
    class Meta:
        model = Vehiculo_Cotizacion
        fields = '__all__'


class CotizaciondireccionForm(ModelForm):
    class Meta:
        model = Cotizacion_direccion
        fields = '__all__'


class CotizaciontrabajadorForm(ModelForm):
    class Meta:
        model = Cotizacion_trabajador
        fields = '__all__'


class CotizacionAmbienteForm(ModelForm):
    class Meta:
        model = Cotizacion_Ambiente
        fields = '__all__'


class CotizacionMuebleForm(ModelForm):
    class Meta:
        model = Cotizacion_Mueble
        fields = '__all__'


class CotizacionServicioForm(ModelForm):
    class Meta:
        model = Cotizacion_Servicio
        fields = '__all__'


class CotizacionMaterialForm(ModelForm):
    class Meta:
        model = Cotizacion_Material
        fields = '__all__'

    def get_form(self, step=None, data=None, files=None):
        form = super(CotizacionMaterialForm, self).get_form(step, data, files)

        # determine the step if not given
        if step is None:
            step = self.steps.current

        if step == '1':
            form.precio_unitario = Material.objects.values('precio').filter(self.request.material)
            form.peso_unitario = 0
        return form


class CotizacionContenidoForm(ModelForm):
    class Meta:
        model = Cotizacion_Contenido
        fields = '__all__'
