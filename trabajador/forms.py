""" Form para Cargos de trabajadores """

from django.forms import ModelForm
from trabajador.models import Cargo_trabajador


class CargotrabajadorForm(ModelForm):
    """Form para ver o editar el cargo del trabajador"""

    class Meta:  # pylint: disable-msg=R0903
        """ Asignación de características específicas al form """
        model = Cargo_trabajador
        fields = '__all__'
        labels = {
            'cargo': ('Rol de trabajador'),
            'tarifa_dia': ('Tarifa por día'),
            'recargo_fin_semana': ('Recargo por trabajo de fin de semana'),
            'recargo_nocturno': ('Recargo por trabajo nocturno')
        }
