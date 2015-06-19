from django.contrib import admin
from cotizacion.models import Estado_Cotizacion, \
    Piso, Tiempo_Carga, Cotizacion, Vehiculo, \
    Vehiculo_Cotizacion, Cotizacion_direccion, \
    Cotizacion_trabajador, Cotizacion_Ambiente, \
    Cotizacion_Mueble, Cotizacion_Servicio, \
    Cotizacion_Material, Cotizacion_Contenido

# Register your models here.
admin.site.register(Estado_Cotizacion)
admin.site.register(Piso)
admin.site.register(Tiempo_Carga)
admin.site.register(Cotizacion)
admin.site.register(Vehiculo)
admin.site.register(Vehiculo_Cotizacion)
admin.site.register(Cotizacion_direccion)
admin.site.register(Cotizacion_trabajador)
admin.site.register(Cotizacion_Ambiente)
admin.site.register(Cotizacion_Mueble)
admin.site.register(Cotizacion_Servicio)
admin.site.register(Cotizacion_Material)
admin.site.register(Cotizacion_Contenido)
