from django.forms import ModelForm
from telefono.models import Tipo_telefono, Telefono


class TipoTelefonoForm(ModelForm):
    class Meta:
        model = Tipo_telefono
        fields = '__all__'
        labels = {
            'tipo_telefono': ('Tipo de teléfono'),
        }


class TelefonoForm(ModelForm):
    class Meta:
        model = Telefono
        fields = '__all__'
        labels = {
            'cliente': ('Nombre del cliente'),
            'tipo_telefono': ('Tipo de teléfono'),
            'numero': ('Número de teléfono'),
        }
