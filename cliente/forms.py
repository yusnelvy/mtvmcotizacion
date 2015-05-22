from django.forms import ModelForm
from cliente.models import Cliente, Email


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        search_fields = ['nombre_principal']


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
