from django.forms import ModelForm
from trabajador.models import Cargo_trabajador


class CargotrabajadorForm(ModelForm):
    class Meta:
        model = Cargo_trabajador
        fields = '__all__'
