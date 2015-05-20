from django.contrib import admin
from ambiente.models import Tipo_ambiente, Ambiente,\
    Ambiente_Tipo_inmueble

# Register your models here.

admin.site.register(Tipo_ambiente)
admin.site.register(Ambiente)
admin.site.register(Ambiente_Tipo_inmueble)
