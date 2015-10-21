"""Docstring"""

from django.forms import ModelForm, ModelChoiceField, RadioSelect, \
    Select, SelectMultiple, TextInput
from presupuesto.models import Presupuesto, Presupuesto_direccion, \
    Presupuesto_Detalle, Presupuesto_servicio, DatosPrecargado
from django.core.exceptions import NON_FIELD_ERRORS
from mueble.models import Ocupacion, Tamano_Mueble, Mueble, Tamano
from direccion.models import Tipo_Inmueble
from ambiente.models import Ambiente
from servicio.models import Servicio, Material
from django import forms
from premisas.models import FuentePromocion
from contenido.models import Contenido


class PresupuestoDetalleForm1(forms.Form):
    """docstring"""
    lista_ambiente = ModelChoiceField(Ambiente.objects, widget=Select, empty_label=None, label='Ambientes')


class PresupuestoDetalleForm2(forms.Form):
    """docstring"""
    lista_mueble = ModelChoiceField(Mueble.objects, widget=Select, empty_label=None, label='Muebles')


class PresupuestoDetalleForm3(forms.Form):
    """docstring"""
    lista_tamano = ModelChoiceField(Tamano_Mueble.objects, widget=Select, label='Tamano')


class PresupuestoForm(ModelForm):
    """Docstring"""
    fuente_choices = [(fuente.fuente_promocion, fuente.fuente_promocion) for fuente in FuentePromocion.objects.all()]

    fecha_estimadamudanza = forms.DateField(
        label='Fecha estimada de la mudanza:',
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'class': 'width50'}),
        input_formats=('%Y-%m-%d', '%d/%m/%Y',))

    fuente_promocion = forms.ChoiceField(
        widget=Select(attrs={'class': 'width50'}),
        label='Fuente de promoción',
        choices=fuente_choices)

    class Meta:
        model = Presupuesto
        fields = '__all__'
        labels = {
            'dni': ('DNI del solicitante:'),
            'nombre_cliente': ('Nombre del solicitante:'),
            'empresa_cliente': ('Empresa donde trabaja el solicitante:'),
            'cargo_cliente': ('Cargo del solicitante:'),
            'telefono_celular': ('Teléfono celular del solicitante:'),
            'telefono': ('Teléfono fijo del solicitante:'),
            'email': ('Email del solicitante:'),
            'fecha_estimadamudanza': ('Fecha estimada de la mudanza:'),
            'hora_estimadamudanza': ('Hora estimada de la mudanza:'),
            'recorrido_km': ('Distancia de traslado en Kms:'),
            'tiempo_recorrido': ('Tiempo de traslado en horas:'),
            'cotizador': ('Cotizador:'),
            'fecha_creacion': ('Fecha de registro:'),
            'hora_creacion': ('Hora de registro:'),
            'comentario': ('Observaciones')
        }
        widgets = {
            'dni': TextInput(
                attrs={
                    'class': 'width50',
                    'onkeypress': 'return justNumbers(event);'
                    }),
            'telefono_celular': TextInput(
                attrs={
                    'class': 'width50',
                    'onkeypress': 'return justNumbers(event);'
                    }),
            'telefono': TextInput(
                attrs={
                    'class': 'width50',
                    'onkeypress': 'return justNumbers(event);'
                    }),
            'email': TextInput(
                attrs={
                    'class': 'width50'
                    }),
            'hora_estimadamudanza': Select(
                attrs={
                    'class': 'width50'
                    }),
            'recorrido_km': Select(
                attrs={
                    'class': 'width50'
                    }),
            'tiempo_recorrido': Select(
                attrs={
                    'class': 'width50'
                    }),
            'fecha_estimadamudanza': TextInput(
                attrs={
                    'class': 'width50'
                    }),
            }

        error_messages = {
            NON_FIELD_ERRORS: {
                'dni': "%(model_name)s's %(field_labels)s esta vacio.",
            }
        }


class PresupuestoDireccionForm(ModelForm):
    """Docstring"""
    lista_tipoinmueble = ModelChoiceField(Tipo_Inmueble.objects, widget=Select(attrs={'class': 'width50'}), empty_label=None, label='Tipo de inmueble:')
    lista_ocupacion = ModelChoiceField(Ocupacion.objects, widget=RadioSelect(attrs={'onclick': 'radioColorBlue(name);'}), empty_label=None, label='Nivel de ocupación del inmueble:')

    class Meta:
        model = Presupuesto_direccion
        fields = 'direccion', \
            'lista_tipoinmueble', \
            'lista_ocupacion', \
            'total_m2', \
            'distancia_vehiculo',\
            'pisos', \
            'pisos_escalera', \
            'rampa', \
            'ascensor', \
            'pisos_ascensor', \
            'ascensor_servicio', \
            'pisos_ascensor_servicio', \
            'presupuesto', \
            'tipo_direccion', \
            'tipo_inmueble', \
            'ocupacidad_inmueble', \
            'valor_ocupacidad', \
            'complejidad', \
            'factor_complejidad', \
            'valor_ambiente_complejidad', \
            'valor_metrocubico_complejiadad',
        labels = {
            'nombre_cliente': ('Nombre del solicitante'),
            'direccion': ('Dirección del inmueble'),
            'ascensor_servicio': ('Ascensor de servicio'),
            'distancia_vehiculo': ('Distancia del inmueble al vehículo (m)'),
            'total_m2': ('Área del inmueble (m2)'),
            'pisos': ('Cantidad de pisos del inmueble'),
            'pisos_escalera': ('Cantidad de pisos a recorrer por escaleras'),
            'pisos_ascensor': ('Cantidad de pisos a recorrer por el ascensor'),
            'pisos_ascensor_servicio': (
            'Cantidad de pisos a recorrer por el ascensor de servicio'
            )
            }
        widgets = {
            'pisos_ascensor': RadioSelect(
                attrs={
                    'class': 'radioselect', 'onclick': 'radioColorBlue(name)'
                    }),
            'pisos_ascensor_servicio': RadioSelect(
                attrs={
                    'class': 'radioselect', 'onclick': 'radioColorBlue(name)'
                    }),
            'pisos': RadioSelect(
                attrs={
                    'class': 'radioselect', 'onclick': 'radioColorBlue(name)'
                    }),
            'pisos_escalera': RadioSelect(
                attrs={
                    'class': 'radioselect', 'onclick': 'radioColorBlue(name);'
                    }),
            'total_m2': Select(
                attrs={
                    'class': 'width50'
                    }),
            'distancia_vehiculo': Select(
                attrs={
                    'class': 'width50'
                    }),
        }
        readonly_fields = ('tipo_direccion')
        error_messages = {
            'nombre_cliente': {
                'required': 'Por favor indique el nombre del solicitante',
            },
        }


class PresupuestoDetalleForm(ModelForm):
    """Docstring"""
    lista_ambiente = ModelChoiceField(Ambiente.objects, widget=Select, empty_label=None, label='Ambiente del inmueble:')
    lista_mueble = ModelChoiceField(Mueble.objects, widget=Select, empty_label=None, label='Mueble del ambiente:')
    lista_tamano = ModelChoiceField(Tamano.objects, widget=RadioSelect, empty_label=None, label='Tamaño del mueble:')
    lista_ocupacion = ModelChoiceField(Ocupacion.objects, widget=RadioSelect, empty_label=None, label='Ocupación del mueble:')

    contenido_choices = [(contenido.contenido, contenido.contenido) for contenido in Contenido.objects.all()]
    descripcion_contenido = forms.ChoiceField(
        widget=Select(attrs={'class': 'width50'}),
        label='Descripción del contenido',
        choices=contenido_choices)

    DENSIDAD_CHOICES = (
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
        ('Muy alta', 'Muy alta'),
    )
    descripcion_densidadcontenido = forms.ChoiceField(
        widget=RadioSelect(attrs={'class': 'radioselect', 'onclick': 'radioColorBlue(name)'}),
        label='Densidad del contenido',
        choices=DENSIDAD_CHOICES)

    contenedor_choices = [(contenedor.material, contenedor.material) for contenedor in Material.objects.filter(contenedor=True)]
    descripcion_contenedor = forms.ChoiceField(
        widget=Select(attrs={'class': 'width50'}),
        label='Descripción del contenedor',
        choices=contenedor_choices)

    class Meta:
        model = Presupuesto_Detalle
        fields = 'lista_ambiente', \
            'lista_mueble', \
            'lista_tamano', \
            'presupuesto', \
            'ambiente', \
            'mueble', \
            'tamano', \
            'ancho', \
            'largo', \
            'alto', \
            'cantidad', \
            'trasladable', \
            'lista_ocupacion', \
            'descripcion_contenido', \
            'descripcion_densidadcontenido', \
            'densidadcontenido', \
            'volumen_contenido', \
            'ocupacidad', \
            'valor_ocupacidad', \
            'cantidad_contenedor', \
            'volumen_contenedor', \
            'volumen_mueble', \
            'capacidad_peso_contenedor', \
            'capacidad_volumen_contenedor', \
            'peso_contenido', \
            'peso_contenedor', \
            'descripcion_contenedor'

        labels = {
            'ancho': ('Ancho del mueble (cms)'),
            'largo': ('Largo del mueble (cms)'),
            'alto': ('Alto del mueble (cms)'),
            'trasladable': ('Mueble trasladable'),
            'densidadcontenido': ('Densidad del contenido (kg/m3)'),
            'volumen_contenido': ('Volumen del contenido (m3)')
            }
        widgets = {
            'ancho': TextInput(
                attrs={
                    'class': 'width50'
                    }),
            'largo': TextInput(
                attrs={
                    'class': 'width50'
                    }),
            'alto': TextInput(
                attrs={
                    'class': 'width50'
                    }),
            'cantidad': TextInput(
                attrs={
                    'class': 'width50',
                    'type': 'number',
                    'step': '1.00'
                    }),
            'densidadcontenido': TextInput(
                attrs={
                    'class': 'width50',
                    }),
            'volumen_contenido': TextInput(
                attrs={
                    'class': 'width50',
                    })
        }


class PresupuestoServicioForm(ModelForm):
    """Docstring"""
    lista_servicio = ModelChoiceField(Servicio.objects.exclude(servicio_material__material__contenedor=True).distinct(), widget=SelectMultiple, empty_label=None, label='Servicios')

    class Meta:
        model = Presupuesto_servicio
        fields = 'lista_servicio', \
            'detalle_presupuesto', \
            'servicio'

        error_messages = {
            NON_FIELD_ERRORS: {
                'servicio': "%(model_name)s's %(field_labels)s está vacío.",
            }
        }


class DatosPrecargadoForm(ModelForm):
    """docstring"""
    class Meta:
        model = DatosPrecargado
        fields = '__all__'


class PresupuestoRevisarForm(ModelForm):
    """docstring"""
    class Meta:
        model = Presupuesto
        fields = 'monto_recursos_revisado', \
                 'monto_vehiculo_revisado', \
                 'monto_servicios_revisado', \
                 'monto_materiales_revisado', \
                 'monto_mundanza_revisada',\
                 'monto_descuento_recargo', \
                 'descuento_recargo', \
                 'tipo_calculo'
        widgets = {
            'monto_mundanza_revisada': TextInput(
                attrs={
                    'required': 'True',
                    'readonly': 'readonly',
                    'class': 'input-re check3 input-re-no-border fuenteSubTotales',
                    'type': 'number',
                    'step': '0.01',
                    'style': 'text-align: right; padding-right: 10px;'
                    }),
            'monto_recursos_revisado': TextInput(
                attrs={
                    'required': 'True',
                    'class': 'input-re check3',
                    'type': 'number',
                    'step': '0.01',
                    'style': 'text-align: right; padding-right: 10px;'
                    }
                ),
            'monto_vehiculo_revisado': TextInput(
                attrs={
                    'required': 'True',
                    'class': 'input-re check3',
                    'type': 'number',
                    'step': '0.01',
                    'style': 'text-align: right; padding-right: 10px;'
                    }
                ),
            'monto_servicios_revisado': TextInput(
                attrs={
                    'required': 'True',
                    'class': 'input-re check3',
                    'type': 'number',
                    'step': '0.01',
                    'style': 'text-align: right; padding-right: 10px;'
                    }
                ),
            'monto_materiales_revisado': TextInput(
                attrs={
                    'required': 'True',
                    'class': 'input-re check3',
                    'type': 'number',
                    'step': '0.01',
                    'style': 'text-align: right; padding-right: 10px;'
                    }
                ),
            'monto_descuento_recargo': TextInput(
                attrs={
                    'required': 'True',
                    'class': 'input-re check3',
                    'type': 'number',
                    'step': '0.01',
                    'style': 'text-align: right; padding-right: 10px;'
                    }
                ),
            'descuento_recargo': TextInput(
                attrs={
                    'hidden': 'hiden'
                }),
            'tipo_calculo': TextInput(
                attrs={
                    'hidden': 'hiden'
                })
        }
