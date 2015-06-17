from django.forms import ModelForm
from ambiente.models import Ambiente, Ambiente_Tipo_inmueble


class AmbienteForm(ModelForm):
    class Meta:
        model = Ambiente
        fields = '__all__'
        labels = {
            'tipo_ambiente': ('Tipo de ambiente'),
        }


class AmbienteTipoInmuebleForm(ModelForm):
    class Meta:
        model = Ambiente_Tipo_inmueble
        fields = '__all__'
