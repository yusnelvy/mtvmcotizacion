from django.forms import ModelForm, DateInput
from cliente.models import Cliente, Email, Sexo, Estado_civil


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        search_fields = ['nombre_principal']
        widgets = {'fecha_nacimiento': DateInput(attrs={'type': "date"})}


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
