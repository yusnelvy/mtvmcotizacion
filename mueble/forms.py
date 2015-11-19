"""
Docstring
Ayuda del mueble/forms.py

"""

from django.forms import ModelForm
from mueble.models import Tipo_Mueble, Ocupacion,\
    Forma_Mueble, Mueble, Tamano, Tamano_Mueble, \
    Mueble_Ambiente, Densidad


class TipoMuebleForm(ModelForm):
    """Docstring"""
    class Meta:
        model = Tipo_Mueble
        fields = '__all__'
        labels = {
            'tipo_mueble': ('Tipo de mueble')
        }


class OcupacionForm(ModelForm):
    """Docstring"""
    class Meta:
        model = Ocupacion
        fields = '__all__'
        labels = {
            'descripcion': ('Nivel de ocupación del mueble'),
            'valor': ('Porcentaje de ocupación del mueble')
        }


class FormaMuebleForm(ModelForm):
    """Docstring"""
    class Meta:
        model = Forma_Mueble
        fields = '__all__'
        labels = {
            'forma': ('Nombre de la forma del mueble')
        }


class MuebleForm(ModelForm):
    """Docstring"""
    def __init__(self, *args, **kwargs):
        super(MuebleForm, self).__init__(*args, **kwargs)
        self.fields['tipo_mueble'].empty_label = "Seleccione el tipo de mueble"
        self.fields['forma'].empty_label = "Seleccione la forma del mueble"
        self.fields['ocupacion'].empty_label = "Seleccione el nivel de ocupación del mueble"

    class Meta:
        model = Mueble
        fields = '__all__'
        labels = {
            'mueble': ('Nombre del mueble'),
            'tipo_mueble': ('Tipo de mueble'),
            'forma': ('Forma del mueble'),
            'ocupacion': ('Nivel de ocupación del mueble'),
            'capacidad': ('Porcentaje de capacidad interna'),
            'trasladable': ('Marcar si el mueble es trasladable'),
            'apilable': ('Marcar si el mueble es apilable'),
            'capacidad_carga': ('Marcar si el mueble aguanta peso'),
            'capacidad_interna': ('Marcar si el mueble puede contener objetos')
        }


class TamanoForm(ModelForm):
    """Docstring"""
    class Meta:
        model = Tamano
        fields = '__all__'
        labels = {
            'descripcion': ('Nombre del tamaño de mueble'),
        }


class DensidadForm(ModelForm):
    """Docstring"""
    class Meta:
        model = Densidad
        fields = '__all__'
        labels = {
            'descripcion': ('Nombre de la densidad de mueble'),
        }


class TamanoMuebleForm(ModelForm):
    """Docstring"""
    def __init__(self, *args, **kwargs):
        super(TamanoMuebleForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Tamano_Mueble
        fields = '__all__'
        labels = {
            'tamano': ('Nombre del tamaño del mueble'),
            'mueble': ('Nombre del mueble'),
            'ancho': ('Ancho del mueble en cms'),
            'largo': ('Largo  del mueble en cms'),
            'alto': ('Alto  del mueble en cms'),
            'predefinido': ('Marcar si este es el tamaño predefinido para este mueble'),
        }


class MuebleAmbienteForm(ModelForm):
    """Docstring"""
    def __init__(self, *args, **kwargs):
        super(MuebleAmbienteForm, self).__init__(*args, **kwargs)
        self.fields['ambiente'].empty_label = "Seleccione el ambiente"
        self.fields['mueble'].empty_label = "Seleccione el mueble"

    class Meta:
        model = Mueble_Ambiente
        fields = '__all__'
        labels = {
            'mueble': ('Nombre del mueble'),
            'ambiente': ('Nombre del ambiente'),
            'predefinido': ('Marcar si este ambiente es predefinido para el mueble'),
        }
