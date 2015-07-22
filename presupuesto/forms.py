"""
Docstring
Ayuda del mueble/forms.py

"""
from django.forms import ModelForm, ModelChoiceField, RadioSelect, Select
from presupuesto.models import Presupuesto, Presupuesto_direccion, Presupuesto_Detalle
from django.core.exceptions import NON_FIELD_ERRORS
from mueble.models import Ocupacion, Tamano_Mueble, Mueble, Tamano
from direccion.models import Tipo_Inmueble
from ambiente.models import Ambiente
from django import forms


class PresupuestoDetalleForm1(forms.Form):
    lista_ambiente = ModelChoiceField(Ambiente.objects, widget=Select, empty_label=None, label='Ambientes')


class PresupuestoDetalleForm2(forms.Form):
    lista_mueble = ModelChoiceField(Mueble.objects, widget=Select, empty_label=None, label='Muebles')


class PresupuestoDetalleForm3(forms.Form):
    lista_tamano = ModelChoiceField(Tamano_Mueble.objects, widget=Select, label='Tamano')


class PresupuestoForm(ModelForm):

    """Docstring"""

    class Meta:
        model = Presupuesto
        fields = '__all__'
        labels = {
            'nombre_cliente': ('Cliente')
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'dni': "%(model_name)s's %(field_labels)s esta vacio.",
            }
        }


class PresupuestoDireccionForm(ModelForm):

    """Docstring"""
    lista_tipoinmueble = ModelChoiceField(Tipo_Inmueble.objects, widget=RadioSelect, empty_label=None, label='Tipo de inmueble')
    lista_ocupacion = ModelChoiceField(Ocupacion.objects, widget=RadioSelect, empty_label=None, label='Ocupación del inmueble')

    class Meta:
        model = Presupuesto_direccion
        fields = 'direccion', \
            'lista_tipoinmueble', \
            'total_m2', \
            'distancia_vehiculo',\
            'lista_ocupacion', \
            'pisos', \
            'pisos_escalera', \
            'rampa', \
            'ascensor', \
            'pisos_ascensor', \
            'ascensor_servicio', \
            'pisos_ascensor_servicio', \
            'presupuesto', \
            'tipo_direccion', \
            'tipo_inmueble', \
            'ocupacidad_inmueble', \
            'valor_ocupacidad', \
            'complejidad', \
            'factor_complejidad', \
            'valor_ambiente_complejidad', \
            'valor_metrocubico_complejiadad'

        labels = {
            'nombre_cliente': ('Cliente'),
        }
        error_messages = {
            'nombre_cliente': {
                'required': 'Please enter your name',
            },
        }


class PresupuestoDetalleForm(ModelForm):

    """Docstring"""

    lista_ambiente = ModelChoiceField(Ambiente.objects, widget=Select, empty_label=None, label='Ambientes')
    lista_mueble = ModelChoiceField(Mueble.objects, widget=Select, empty_label=None, label='Muebles')
    lista_tamano = ModelChoiceField(Tamano.objects, widget=Select, label='Tamano')
    lista_ocupacion = ModelChoiceField(Ocupacion.objects, widget=RadioSelect, empty_label=None, label='Ocupación del inmueble')

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
            'peso_contenedor'
