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
            'cargo': ('Nombre del rol o cargo de trabajador'),
            'tarifa_dia': ('Tarifa ($/día)'),
            'recargo_fin_semana': ('Porcentaje de recargo por trabajo de fin de semana'),
            'recargo_nocturno': ('Porcentaje de recargo por trabajo nocturno')
        }
