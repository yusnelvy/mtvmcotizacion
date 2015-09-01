"""
  docstring para las URLS

  Documentación por desarrollar
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',  # C0103: El error es la forma del nombre urlpatterns pero no se puede corregir
                       url(r'^', include('inicio.urls', namespace='uinicio')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^ambiente/', include('ambiente.urls', namespace="uambientes")),
                       url(r'^chaining/', include('smart_selects.urls')),
                       url(r'^cliente/', include('cliente.urls', namespace="uclientes")),
                       url(r'^contenido/', include('contenido.urls', namespace="ucontenidos")),
                       url(r'^cotizacion/', include('cotizacion.urls', namespace="ucotizaciones")),
                       url(r'^direccion/', include('direccion.urls', namespace="udirecciones")),
                       url(r'^mueble/', include('mueble.urls', namespace="umuebles")),
                       url(r'^presupuesto/', include('presupuesto.urls', namespace="upresupuestos")),
                       url(r'^servicio/', include('servicio.urls', namespace="uservicios")),
                       url(r'^telefono/', include('telefono.urls', namespace="utelefonos")),
                       url(r'^trabajador/', include('trabajador.urls', namespace="utrabajadores")),
                      )

# se agrego para probar los estilo
if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': settings.STATICFILES_DIRS}),)
