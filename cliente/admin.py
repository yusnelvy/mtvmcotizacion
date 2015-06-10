from django.contrib import admin
from cliente.models import Cliente, Email, Sexo, Estado_civil

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Email)
admin.site.register(Sexo)
admin.site.register(Estado_civil)
