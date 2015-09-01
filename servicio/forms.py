"""docstring"""
from django.forms import ModelForm, TextInput
from servicio.models import Servicio, Material, \
    Servicio_Material, Complejidad, \
    Complejidad_Servicio, Unidad


class ServicioForm(ModelForm):
    """docstring"""
    class Meta:
        model = Servicio
        fields = '__all__'
        labels = {
            'servicio': ('Nombre del servicio')
        }


class MaterialForm(ModelForm):
    """docstring"""
    class Meta:
        model = Material
        fields = [
            'material',
            'unidad',
            'ancho',
            'largo',
            'alto',
            'peso',
            'precio',
            'contenedor',
            'capacidad_peso',
            'capacidad_volumen'
        ]
        labels = {
            'material': ('Nombre del material'),
            'precio': ('Precio unitario del material'),
            'peso': ('Peso unitario del material'),
            'recuperable': ('Marcar si el material es recuperable luego de su uso'),
            'ancho': ('Ancho del material (cms)'),
            'largo': ('Largo del material (cms)'),
            'alto': ('Alto del material (cms)'),
            'capacidad_peso': ('Capacidad de contener objetos (kg)'),
            'capacidad_volumen': ('Capacidad de contener objetos (m3)'),
            'contenedor': ('Marcar si el material es contenedor'),
            'unidad': ('Unidad de medida'),
        }


class ServicioMaterialForm(ModelForm):
    """docstring"""
    class Meta:
        model = Servicio_Material
        fields = '__all__'
        labels = {
            'servicio': ('Nombre del servicio'),
            'material': ('Nombre del material'),
            'cantidad': ('Cantidad de material aplicado al servicio'),
            'Calculo': ('Forma de cálculo del material consumido')
            }
        widgets = {
            'cantidad': TextInput(attrs={'readonly': 'readonly'})
        }


class ComplejidadForm(ModelForm):
    """docstring"""
    class Meta:
        model = Complejidad
        fields = '__all__'
        labels = {
            'descripcion': ('Nivel de complejidad')
        }


class ComplejidadServicioForm(ModelForm):
    """docstring"""
    class Meta:
        model = Complejidad_Servicio
        fields = '__all__'
        labels = {
            'complejidad': ('Nivel de complejidad'),
            'tarifa': ('Tarifa aplicable'),
            'servicio': ('Nombre del servicio'),
            'factor_tiempo': ('Factor de aplicación de tiempo para prestar el servicio')
        }


class UnidadForm(ModelForm):
    """docstring"""
    class Meta:
        model = Unidad
        fields = '__all__'
        labels = {
            'unidad': ('Unidad de medida')
        }
