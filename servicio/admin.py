from django.contrib import admin
from servicio.models import Servicio, Material, \
    Servicio_Material, Complejidad, Complejidad_Servicio

# Register your models here.
admin.site.register(Servicio)
admin.site.register(Material)
admin.site.register(Servicio_Material)
admin.site.register(Complejidad)
admin.site.register(Complejidad_Servicio)
