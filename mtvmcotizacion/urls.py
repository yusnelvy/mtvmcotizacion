"""
  docstring para las URLS

  Documentación por desarrollar
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
#from haystack.views import SearchView


urlpatterns = patterns('',  # C0103: El error es la forma del nombre urlpatterns pero no se puede corregir
                       # Examples:
                       # url(r'^$', 'mtvmcotizacion.views.home', name='home'),
                       # url(r'^blog/', inclde('blog.urls')),

                       url(r'^', include('inicio.urls', namespace='uinicio')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^direccion/', include('direccion.urls', namespace="udireciones")),
                       url(r'^telefono/', include('telefono.urls', namespace="utelefonos")),
                       url(r'^cliente/', include('cliente.urls', namespace="uclientes")),
                       url(r'^ambiente/', include('ambiente.urls', namespace="uambientes")),
                       url(r'^servicio/', include('servicio.urls', namespace="uservicios")),
                       url(r'^mueble/', include('mueble.urls', namespace="umuebles")),
                       url(r'^contenido/', include('contenido.urls', namespace="ucontenidos")),
                       url(r'^trabajador/', include('trabajador.urls', namespace="utrabajadores")),
                       url(r'^cotizacion/', include('cotizacion.urls', namespace="ucotizaciones")),
                       url(r'^chaining/', include('smart_selects.urls')),
                       #url(r'^search/', SearchView(load_all=False)),
                       #url(r'^search/', include('haystack.urls')),
                       )

# se agrego para probar los estilo
if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': settings.STATICFILES_DIRS}),)
