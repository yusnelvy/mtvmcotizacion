from django.forms import ModelForm
from ambiente.models import Ambiente, Ambiente_Tipo_inmueble


class AmbienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Ambiente
        fields = '__all__'
        labels = {
            'ambiente': ('Nombre del ambiente'),
        }


class AmbienteTipoInmuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(AmbienteTipoInmuebleForm, self).__init__(*args, **kwargs)
        self.fields['ambiente'].empty_label = "Seleccione el ambiente"

    class Meta:
        model = Ambiente_Tipo_inmueble
        fields = '__all__'
        labels = {
            'ambiente': ('Nombre del ambiente'),
            'tipo_inmueble': ('Nombre del tipo de inmueble'),
        }
