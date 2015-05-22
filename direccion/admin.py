from django.contrib import admin
from direccion.models import Pais, Provincia, Ciudad, \
    Zona, Tipo_direccion, Direccion, Tipo_Inmueble, \
    Complejidad_Inmueble, Inmueble

# Register your models here.
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Zona)
admin.site.register(Tipo_direccion)
admin.site.register(Direccion)
admin.site.register(Tipo_Inmueble)
admin.site.register(Complejidad_Inmueble)
admin.site.register(Inmueble)
