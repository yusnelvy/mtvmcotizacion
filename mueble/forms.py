from django.forms import ModelForm
from mueble.models import Tipo_Mueble, Ocupacion,\
    Forma_Mueble, Mueble, Tamano, Tamano_Mueble, \
    Mueble_Ambiente


class TipoMuebleForm(ModelForm):
    class Meta:
        model = Tipo_Mueble
        fields = '__all__'


class OcupacionForm(ModelForm):
    class Meta:
        model = Ocupacion
        fields = '__all__'


class FormaMuebleForm(ModelForm):
    class Meta:
        model = Forma_Mueble
        fields = '__all__'


class MuebleForm(ModelForm):
    class Meta:
        model = Mueble
        fields = '__all__'


class TamanoForm(ModelForm):
    class Meta:
        model = Tamano
        fields = '__all__'


class TamanoMuebleForm(ModelForm):
    class Meta:
        model = Tamano_Mueble
        fields = '__all__'


class MuebleAmbienteForm(ModelForm):
    class Meta:
        model = Mueble_Ambiente
        fields = '__all__'
