from django.forms import ModelForm
from contenido.models import Contenido, \
    Contenido_Tipico, Contenido_Servicio


class ContenidoForm(ModelForm):
    """docstring"""
    class Meta:
        model = Contenido
        fields = '__all__'
        labels = {
            'contenido': ('Tipo de contenido'),
            'densidad_baja': ('Densidad baja en Kgs/m3'),
            'densidad_media': ('Densidad media en Kgs/m3'),
            'densidad_alta': ('Densidad alta en Kgs/m3'),
            'densidad_superalta': ('Densidad super-alta en Kgs/m3')
        }


class ContenidoTipicoForm(ModelForm):
    """docstring"""
    class Meta:
        model = Contenido_Tipico
        fields = '__all__'
        labels = {
            'contenido': ('Tipo de contenido'),
            'mueble': ('Nombre del mueble'),
            'cantidad': ('Porcentaje de la capacidad del mueble que ocupa este contenido'),
            'predefinido': ('Marcar si este contenido es el predefinido para el mueble'),
        }


class ContenidoServicioForm(ModelForm):
    """docstring"""
    class Meta:
        model = Contenido_Servicio
        fields = '__all__'
        labels = {
            'contenido': ('Tipo de contenido'),
            'servicio': ('Nombre del servicio'),
            'predefinido': ('Marcar si este servicio es el predefinido para el contenido'),
        }
