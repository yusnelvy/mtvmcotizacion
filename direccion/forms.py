"""
Docstring documentación pendiente

"""

from django.forms import ModelForm, TextInput
from direccion.models import Pais, Provincia, Ciudad, \
    Zona, Tipo_direccion, Direccion, Tipo_Inmueble, \
    Complejidad_Inmueble, Inmueble
from haystack.forms import SearchForm


class PaisForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Pais
        fields = '__all__'
        labels = {
            'pais': ('País')
        }


class ProvinciaForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Provincia
        fields = '__all__'
        labels = {
            'provincia': ('Provincia'),
            'pais': ('País')
        }


class CiudadForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Ciudad
        fields = '__all__'
        labels = {
            'ciudad': ('Ciudad'),
            'provincia': ('Provincia'),
            'pais': ('País')
        }


class ZonaForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Zona
        fields = '__all__'
        labels = {
            'zona': ('Zona'),
            'ciudad': ('Ciudad'),
            'provincia': ('Provincia'),
            'pais': ('País')
        }


class DireccionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Direccion
        fields = '__all__'
        labels = {
            'Calle': ('Calle'),
            'numero': ('Número'),
            'piso': ('Piso'),
            'adicional': ('Información adicional'),
            'tipo_direccion': ('Tipo de dirección'),
            'pais': ('País'),
            'provincia': ('Provincia'),
            'ciudad': ('Ciudad'),
            'zona': ('Zona'),
            'zip1': ('Código postal / Zip'),
            'punto_referencia': ('Punto de referencia'),
            'cliente': ('Cliente')
        }


class TipoDireccionForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Tipo_direccion
        fields = '__all__'
        labels = {
            'tipo_direccion': ('Nombre del tipo de dirección'),
            'activo': ('Marcar si el tipo de dirección está activo o inactivo')
            }


class TipoInmuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Tipo_Inmueble
        fields = '__all__'
        labels = {
            'tipo_inmueble': ('Nombre del tipo de inmueble')
        }


class ComplejidadInmuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Complejidad_Inmueble
        fields = '__all__'
        labels = {
            'complejidad': ('Nivel de complejidad del inmueble'),
            'factor': ('Factor de complejidad del inmueble'),
            'valor_ambiente': ('Tarifa de mudanza por ambiente'),
            'valor_metrocubico': ('Tarifa de mudanza por m3')
        }


class InmuebleForm(ModelForm):
    """
    Docstring documentación pendiente
    """
    class Meta:
        model = Inmueble
        fields = '__all__'
        labels = {
            'inmueble': ('Nombre del inmueble'),
            'tipo_inmueble': ('Tipo  de inmueble'),
            'direccion': ('Dirección del inmueble'),
            'numero_ambientes': ('N° de ambientes'),
            'pisos': ('N° de pisos internos del inmueble'),
            'pisos_escalera': ('N° de pisos a recorrer por escaleras para llegar al inmueble'),
            'ascensor': ('Marcar si el inmueble cuenta con ascensor'),
            'ascensor_servicio': ('Marcar si el inmueble cuenta con ascensor de servicio'),
            'pisos_ascensor_servicio': ('N° de pisos a recorrer por ascensor de servicio'),
            'pisos_ascensor': ('N° de pisos a recorrer por ascensor'),
            'complejidad': ('Nivel de complejidad del inmueble'),
            'distancia_vehiculo': ('Distancia desde el inmueble al vehículo de carga'),
        }


#formularios de busqueda
class SearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()
