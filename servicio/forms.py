"""docstring"""
from django.forms import ModelForm, TextInput
from servicio.models import Servicio, Material, \
    Servicio_Material, Complejidad, \
    Complejidad_Servicio, Unidad
from django import forms


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
    def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)
        self.fields['unidad'].empty_label = "Seleccione la unidad"

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
            'capacidad_volumen',
            'recuperable'
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

    def clean_capacidad_peso(self):
        diccionario_limpio = self.cleaned_data

        capacidad_peso = diccionario_limpio.get('capacidad_peso')
        contenedor = diccionario_limpio.get('contenedor')

        if contenedor:
            if capacidad_peso <= 0:
                raise forms.ValidationError("La capacidad de contener objetos (m3) debe ser mayor a cero")

        return capacidad_peso

    def clean_capacidad_volumen(self):
        diccionario_limpio = self.cleaned_data

        capacidad_volumen = diccionario_limpio.get('capacidad_volumen')
        contenedor = diccionario_limpio.get('contenedor')

        if contenedor:
            if capacidad_volumen <= 0:
                raise forms.ValidationError("La capacidad de contener objetos (kg) debe ser mayor a cero")

        return capacidad_volumen


class ServicioMaterialForm(ModelForm):
    """docstring"""
    def __init__(self, *args, **kwargs):
        super(ServicioMaterialForm, self).__init__(*args, **kwargs)
        self.fields['material'].empty_label = "Seleccione el material"

    class Meta:
        model = Servicio_Material
        fields = '__all__'
        labels = {
            'servicio': ('Nombre del servicio'),
            'material': ('Nombre del material'),
            'cantidad': ('Cantidad de material aplicado al servicio'),
            'calculo': ('Forma de cálculo del material consumido')
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
    def __init__(self, *args, **kwargs):
        super(ComplejidadServicioForm, self).__init__(*args, **kwargs)
        self.fields['complejidad'].empty_label = "Seleccione el nivel de complejidad"

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
