"""
Docstring
Ayuda del mueble/forms.py

"""
from django.forms import ModelForm, ModelChoiceField, RadioSelect, Select, SelectMultiple, DateInput
from presupuesto.models import Presupuesto, Presupuesto_direccion, Presupuesto_Detalle, Presupuesto_servicio
from django.core.exceptions import NON_FIELD_ERRORS
from mueble.models import Ocupacion, Tamano_Mueble, Mueble, Tamano
from direccion.models import Tipo_Inmueble
from ambiente.models import Ambiente
from servicio.models import Servicio, Material
from django import forms


class PresupuestoDetalleForm1(forms.Form):
    lista_ambiente = ModelChoiceField(Ambiente.objects, widget=Select, empty_label=None, label='Ambientes')


class PresupuestoDetalleForm2(forms.Form):
    lista_mueble = ModelChoiceField(Mueble.objects, widget=Select, empty_label=None, label='Muebles')


class PresupuestoDetalleForm3(forms.Form):
    lista_tamano = ModelChoiceField(Tamano_Mueble.objects, widget=Select, label='Tamano')


class PresupuestoForm(ModelForm):

    """Docstring"""
    fecha_estimadamudanza = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d'), input_formats=('%Y-%m-%d',))

    class Meta:
        model = Presupuesto
        #widgets = {'fecha_estimadamudanza': DateInput(attrs={'type': 'date'})}
        fields = '__all__'
        labels = {
            'nombre_cliente': ('Nombre del cliente:'),
            'dni': ('DNI del cliente:'),
            'recorrido_km': ('Recorrido en kilómetros de la mudanza:'),
            'tiempo_recorrido': ('Tiempo recorrido de la mudanza:'),
            'fecha_estimadamudanza': ('Fecha estimada de la mudanza:'),
            'telefono': ('Teléfono del cliente:'),
            'email': ('Email del cliente:')
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'dni': "%(model_name)s's %(field_labels)s esta vacio.",
            }
        }


class PresupuestoDireccionForm(ModelForm):

    """Docstring"""
    lista_tipoinmueble = ModelChoiceField(Tipo_Inmueble.objects, widget=Select, empty_label=None, label='Tipo de inmueble:')
    lista_ocupacion = ModelChoiceField(Ocupacion.objects, widget=Select, empty_label=None, label='Nivel de ocupación del inmueble:')

    class Meta:
        model = Presupuesto_direccion
        #widgets = {'pisos': forms.RadioSelect}
        fields = 'direccion', \
            'lista_tipoinmueble', \
            'lista_ocupacion', \
            'total_m2', \
            'distancia_vehiculo',\
            'pisos', \
            'pisos_escalera', \
            'rampa', \
            'ascensor', \
            'ascensor_servicio', \
            'pisos_ascensor', \
            'pisos_ascensor_servicio', \
            'presupuesto', \
            'tipo_direccion', \
            'tipo_inmueble', \
            'ocupacidad_inmueble', \
            'valor_ocupacidad', \
            'complejidad', \
            'factor_complejidad', \
            'valor_ambiente_complejidad', \
            'valor_metrocubico_complejiadad',
        labels = {
            'nombre_cliente': ('Cliente'),
            'direccion': ('Dirección del inmueble:'),
            'ascensor_servicio': ('Ascensor de servicio'),
            'distancia_vehiculo': ('Distancia del inmueble al vehículo (m):'),
            'total_m2': ('Metros cuadrado del inmueble (m2):'),
            'pisos': ('Cantidad de pisos del inmueble:'),
            'pisos_escalera': ('Cantidad de pisos a recorrer por escaleras:'),
            'pisos_ascensor': ('Cantidad de pisos a recorrer por el ascensor:'),
            'pisos_ascensor_servicio': ('Cantidad de pisos a recorrer por el ascensor de servicio:'),
            }
        readonly_fields = ('tipo_direccion')
        error_messages = {
            'nombre_cliente': {
                'required': 'Please enter your name',
            },
        }


class PresupuestoDetalleForm(ModelForm):

    """Docstring"""

    lista_ambiente = ModelChoiceField(Ambiente.objects, widget=Select, empty_label='--seleccione el ambiente--', label='Ambiente del inmueble:')
    lista_mueble = ModelChoiceField(Mueble.objects, widget=Select, empty_label='seleccione el mueble', label='Mueble del ambiente:')
    lista_tamano = ModelChoiceField(Tamano.objects, widget=RadioSelect, empty_label=None, label='Tamaño del mueble:')
    lista_ocupacion = ModelChoiceField(Ocupacion.objects, widget=RadioSelect, empty_label=None, label='Ocupación del mueble:')

    class Meta:
        model = Presupuesto_Detalle
        fields = 'lista_ambiente', \
            'lista_mueble', \
            'lista_tamano', \
            'lista_ocupacion', \
            'presupuesto', \
            'ambiente', \
            'mueble', \
            'tamano', \
            'ancho', \
            'largo', \
            'alto', \
            'densidad', \
            'valor_densidad', \
            'peso', \
            'ocupacidad', \
            'valor_ocupacidad', \
            'cantidad_contenedor', \
            'volumen_contenido', \
            'volumen_contenedor', \
            'volumen_mueble', \
            'capacidad_peso_contenedor', \
            'capacidad_volumen_contenedor', \
            'peso_contenido', \
            'peso_contenedor', \
            'descripcion_contenedor'
        labels = {
            'ancho': ('Ancho del mueble:'),
            'largo': ('Largo del mueble:'),
            'alto': ('Alto del mueble:'),
            }


class PresupuestoServicioForm(ModelForm):

    """Docstring"""
    lista_servicio = ModelChoiceField(Servicio.objects.exclude(servicio_material__material__contenedor=True).distinct(), widget=Select, empty_label=None, label='Servicios')

    class Meta:
        model = Presupuesto_servicio
        fields = 'lista_servicio', \
            'detalle_presupuesto', \
            'servicio'

        error_messages = {
            NON_FIELD_ERRORS: {
                'servicio': "%(model_name)s's %(field_labels)s esta vacio.",
            }
        }
