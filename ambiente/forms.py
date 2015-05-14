from django.forms import ModelForm
from ambiente.models import Tipo_ambiente, \
    Ambiente, Ambiente_Tipo_inmueble


class TipoAmbienteForm(ModelForm):
    class Meta:
        model = Tipo_ambiente
        fields = '__all__'


class AmbienteForm(ModelForm):
    class Meta:
        model = Ambiente
        fields = '__all__'


class AmbienteTipoInmuebleForm(ModelForm):
    class Meta:
        model = Ambiente_Tipo_inmueble
        fields = '__all__'
