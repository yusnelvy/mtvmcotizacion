"""
Docstring pendiente para este documento
"""

from django.conf.urls import patterns, url
from ambiente import views


urlpatterns = patterns('',
                       url(r'^$',
                           views.lista_ambiente,
                           name='lista_ambiente'),
                       url(r'^buscar/(?P<id_tipoinmueble>\d+)/$',
                           views.buscar_ambiente,
                           name='buscar_ambiente'),
                       url(r'^nuevo',
                           views.add_ambiente,
                           name='add_ambiente'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           views.edit_ambiente,
                           name='edit_ambiente'),
                       url(r'^ambiente_tipo_inmueble/$',
                           views.lista_ambiente_tipo_inmueble,
                           name='lista_ambiente_tipo_inmueble'),
                       url(r'^ambiente_tipo_inmueble/nuevo/(?P<id_ti>\d+)/(?P<origen>\d+)/$',
                           views.add_ambiente_tipoinmueble,
                           name='add_ambiente_tipoinmueble'),
                       url(r'^ambiente_tipo_inmueble/editar/(?P<pk>\d+)/$',
                           views.edit_ambiente_tipoinmueble,
                           name='edit_ambiente_tipoinmueble'),)
