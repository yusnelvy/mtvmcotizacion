from django.forms import ModelForm
from telefono.models import Tipo_telefono, Telefono


class TipoTelefonoForm(ModelForm):
    class Meta:
        model = Tipo_telefono
        fields = '__all__'


class TelefonoForm(ModelForm):
    class Meta:
        model = Telefono
        fields = '__all__'
