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
            'descripcion': ('Nivel de ocupación')
        }


class FormaMuebleForm(ModelForm):

    """Docstring"""

    class Meta:
        model = Forma_Mueble
        fields = '__all__'


class MuebleForm(ModelForm):

    """Docstring"""

    class Meta:
        model = Mueble
        fields = '__all__'


class TamanoForm(ModelForm):

    """Docstring"""

    class Meta:
        model = Tamano
        fields = '__all__'


class DensidadForm(ModelForm):

    """Docstring"""

    class Meta:
        model = Densidad
        fields = '__all__'


class TamanoMuebleForm(ModelForm):

    """Docstring"""

    class Meta:
        model = Tamano_Mueble
        fields = '__all__'


class MuebleAmbienteForm(ModelForm):

    """Docstring"""

    class Meta:
        model = Mueble_Ambiente
        fields = '__all__'
