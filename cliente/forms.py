"""
Docstring documentación pendiente
"""

from django.forms import ModelForm, TextInput
from cliente.models import Cliente, Email, Sexo, Estado_civil
from django import forms


class ClienteForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['sexo'].empty_label = "Seleccione el sexo"
        self.fields['estado_civil'].empty_label = "Seleccione el estado civil"

    fecha_nacimiento = forms.DateField(
        label='Fecha de nacimiento:',
        widget=forms.DateInput(format='%d-%m-%Y', attrs={'class': ''}),
        input_formats=('%Y-%m-%d', '%d/%m/%Y',))

    class Meta:
        model = Cliente
        fields = '__all__'
        search_fields = ['nombre_principal']
        #widgets = {'fecha_nacimiento': TextInput(attrs={'type': "text"})}
        labels = {
            'nombre_principal': ('Nombre del cliente'),
            'dni': ('DNI - Documento Nacional de Identificación'),
            'sexo': ('Sexo'),
            'estado_civil': ('Estado civil'),
            'fecha_nacimiento': ('Fecha de nacimiento'),
            'comentarios': ('Comentarios'),
            'adicional1': ('Información adicional 1'),
            'adicional2': ('Información adicional 2'),
            'adicional3': ('Información adicional 3'),
            'adicional4': ('Información adicional 4'),
            'activo': ('Cliente activo (chequeado)')
        }


class EmailForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Email
        fields = '__all__'
        labels = {
            'email': ('Dirección de e-mail'),
            'Cliente': ('Nombre del cliente')
        }


class SexoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Sexo
        fields = '__all__'


class EstadoCivilForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Estado_civil
        fields = '__all__'
        labels = {
            'estado_civil': ('Nombre del Estado civil')
        }
