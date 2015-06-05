from django.forms import ModelForm
from cliente.models import Cliente, Email, Sexo, Estado_civil


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        search_fields = ['nombre_principal']


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = '__all__'


class SexoForm(ModelForm):
    class Meta:
        model = Sexo
        fields = '__all__'


class EstadoCivilForm(ModelForm):
    class Meta:
        model = Estado_civil
        fields = '__all__'
