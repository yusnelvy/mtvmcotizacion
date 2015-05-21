from django.forms import ModelForm
from contenido.models import Contenedor, \
    Contenido, Contenido_Tipico


class ContenedorForm(ModelForm):
    class Meta:
        model = Contenedor
        fields = '__all__'


class ContenidoForm(ModelForm):
    class Meta:
        model = Contenido
        fields = '__all__'


class ContenidoTipicoForm(ModelForm):
    class Meta:
        model = Contenido_Tipico
        fields = '__all__'
