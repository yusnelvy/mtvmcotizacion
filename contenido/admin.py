from django.contrib import admin
from contenido.models import Contenedor, \
    Contenido, Contenido_Tipico

# Register your models here.
admin.site.register(Contenedor)
admin.site.register(Contenido)
admin.site.register(Contenido_Tipico)
