"""Docstring"""
from django.forms import ModelForm, TextInput, Select
from gestiondocumento.models import Estado, EstadoDocumento


class EstadoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Estado
        fields = '__all__'
        widgets = {
            'estado': TextInput(
                attrs={
                    'required': 'required'
                    })
            }


class EstadoDocumentoForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    def __init__(self, *args, **kwargs):
        super(EstadoDocumentoForm, self).__init__(*args, **kwargs)
        self.fields['estado'].empty_label = "Seleccione el estado"

    class Meta:
        model = EstadoDocumento
        fields = '__all__'
        widgets = {
            'estado': Select(
                attrs={
                    'required': 'required'
                    }),
            'orden': TextInput(
                attrs={
                    'required': 'required'
                    }),
            'documento': TextInput(
                attrs={
                    'required': 'required'
                    })
            }
