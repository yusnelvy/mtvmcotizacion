from django.forms import ModelForm
from contenido.models import Contenedor, \
    Contenido, Contenido_Tipico


class ContenedorForm(ModelForm):
    class Meta:
        model = Contenedor
        fields = '__all__'
        labels = {
            'contenedor': ('Tipo de contenedor'),
            'capacidad_volumen': ('Capacidad de volúmen en m3'),
            'capacidad_peso': ('Capacidad de peso en Kgs'),
            'volumen_contenedor': ('Volúmen propio en m3'),
            'peso_contenedor': ('Peso propio en Kgs'),
            'retornable': ('Retornable')
        }


class ContenidoForm(ModelForm):
    class Meta:
        model = Contenido
        fields = '__all__'
        labels = {
            'contenido': ('Tipo de contenido'),
            'contenedor': ('Contenedor propuesto'),
            'densidad_baja': ('Densidad baja en Kgs/m3'),
            'densidad_media': ('Densidad media en Kgs/m3'),
            'densidad_alta': ('Densidad alta en Kgs/m3'),
            'densidad_superalta': ('Densidad super-alta en Kgs/m3')
        }


class ContenidoTipicoForm(ModelForm):
    class Meta:
        model = Contenido_Tipico
        fields = '__all__'
