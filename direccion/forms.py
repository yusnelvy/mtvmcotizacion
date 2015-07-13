from django.forms import ModelForm
from direccion.models import Pais, Provincia, Ciudad, \
    Zona, Tipo_direccion, Direccion, Tipo_Inmueble, \
    Complejidad_Inmueble, Inmueble

#from haystack.forms import SearchForm


class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'
        labels = {'pais': ('País')}


class ProvinciaForm(ModelForm):
    class Meta:
        model = Provincia
        fields = '__all__'


class CiudadForm(ModelForm):
    class Meta:
        model = Ciudad
        fields = '__all__'


class ZonaForm(ModelForm):
    class Meta:
        model = Zona
        fields = '__all__'


class DireccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = '__all__'


class TipoDireccionForm(ModelForm):
    class Meta:
        model = Tipo_direccion
        fields = '__all__'


class TipoInmuebleForm(ModelForm):
    class Meta:
        model = Tipo_Inmueble
        fields = '__all__'


class ComplejidadInmuebleForm(ModelForm):
    class Meta:
        model = Complejidad_Inmueble
        fields = '__all__'
        labels = {
            'valor_ambiente': ('Valor por ambiente'),
            'valor_metrocubico': ('Valor por m3')}


class InmuebleForm(ModelForm):
    class Meta:
        model = Inmueble
        fields = '__all__'

#class PaisSearchForm(SearchForm):


#class PaisSearchForm(SearchForm):

   #d ef no_query_found(self):
      # return self.searchqueryset.all()
