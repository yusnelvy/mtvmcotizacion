from django.forms import ModelForm
from servicio.models import Servicio, Material, \
    Servicio_Material, Complejidad, Complejidad_Servicio


class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = '__all__'


class ServicioMaterialForm(ModelForm):
    class Meta:
        model = Servicio_Material
        fields = '__all__'


class ComplejidadForm(ModelForm):
    class Meta:
        model = Complejidad
        fields = '__all__'
        labels = {
            'descripcion': ('Nivel de complejidad')
        }


class ComplejidadServicioForm(ModelForm):
    class Meta:
        model = Complejidad_Servicio
        fields = '__all__'
