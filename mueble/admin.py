from django.contrib import admin
from mueble.models import Tipo_Mueble, Ocupacion,\
    Forma_Mueble, Mueble, Tamano, Tamano_Mueble, \
    Mueble_Ambiente, Densidad
from mueble.resources import MuebleResource
from import_export.admin import ImportExportModelAdmin


class MuebleAdmin(ImportExportModelAdmin):
    resource_class = MuebleResource
    pass

# Register your models here.
admin.site.register(Tipo_Mueble)
admin.site.register(Ocupacion)
admin.site.register(Forma_Mueble)
admin.site.register(Mueble, MuebleAdmin)
admin.site.register(Tamano)
admin.site.register(Tamano_Mueble)
admin.site.register(Mueble_Ambiente)
admin.site.register(Densidad)
