from django.forms import ModelForm
from cotizacion.models import Estado_Cotizacion, \
    Piso, Tiempo_Carga, Cotizacion, Vehiculo, \
    Vehiculo_Cotizacion, Cotizacion_direccion, \
    Cotizacion_trabajador, Cotizacion_Ambiente, \
    Cotizacion_Mueble, Cotizacion_Servicio, \
    Cotizacion_Material, Cotizacion_Contenedor, \
    Cotizacion_Contenido


class EstadoCotizacionForm(ModelForm):
    class Meta:
        model = Estado_Cotizacion
        fields = '__all__'


class PisoForm(ModelForm):
    class Meta:
        model = Piso
        fields = '__all__'


class TiempoCargaForm(ModelForm):
    class Meta:
        model = Tiempo_Carga
        fields = '__all__'


class CotizacionForm(ModelForm):
    class Meta:
        model = Cotizacion
        fields = '__all__'


class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'


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


class CotizacionContenedorForm(ModelForm):
    class Meta:
        model = Cotizacion_Contenedor
        fields = '__all__'


class CotizacionContenidoForm(ModelForm):
    class Meta:
        model = Cotizacion_Contenido
        fields = '__all__'
