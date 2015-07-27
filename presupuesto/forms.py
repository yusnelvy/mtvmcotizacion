"""
Docstring
Ayuda del mueble/forms.py

"""

from django.forms import ModelForm, Select, ModelChoiceField, RadioSelect
from presupuesto.models import Presupuesto, Presupuesto_direccion, Presupuesto_Detalle
from django.core.exceptions import NON_FIELD_ERRORS
from mueble.models import Ocupacion
from direccion.models import Tipo_Inmueble


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
    lista_tipoinmueble = ModelChoiceField(Tipo_Inmueble.objects, widget=RadioSelect, empty_label=None, label='Tipo de inmueble:')
    lista_ocupacion = ModelChoiceField(Ocupacion.objects, widget=RadioSelect, empty_label=None, label='Nivel de ocupación del inmueble:')

    class Meta:
        model = Presupuesto_direccion
        fields = 'direccion', \
            'lista_tipoinmueble', \
            'lista_ocupacion', \
            'rampa', \
            'ascensor', \
            'ascensor_servicio', \
            'distancia_vehiculo',\
            'total_m2', \
            'pisos', \
            'pisos_escalera', \
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
            'valor_metrocubico_complejiadad'
        labels = {
            'nombre_cliente': ('Cliente'),
            'direccion': ('Dirección del inmueble'),
            }
        readonly_fields = ('tipo_direccion')
        error_messages = {
            'nombre_cliente': {
                'required': 'Please enter your name',
            },
        }


class PresupuestoDetalleForm(ModelForm):

    """Docstring"""

    class Meta:
        model = Presupuesto_Detalle
        fields = '__all__'
