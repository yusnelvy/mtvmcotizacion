"""Docstring"""

from django.conf.urls import patterns, url
from servicio import views


urlpatterns = patterns('',
                       url(r'^$',
                           views.lista_servicio,
                           name='lista_servicio'),
                       url(r'^nuevo',
                           views.add_servicio,
                           name='add_servicio'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           views.edit_servicio,
                           name='edit_servicio'),
                       url(r'^search/$',
                           views.search_servicio,
                           name='search_servicio'),
                       url(r'^contenedor/$',
                           views.lista_contenedor,
                           name='lista_contenedor'),
                       url(r'^material/$',
                           views.lista_material,
                           name='lista_material'),
                       url(r'^material/nuevo',
                           views.add_material,
                           name='add_material'),
                       url(r'^material/editar/(?P<pk>\d+)/$',
                           views.edit_material,
                           name='edit_material'),
                       url(r'^material/search',
                           views.search_material,
                           name='search_material'),
                       url(r'^complejidad/$',
                           views.lista_complejidad,
                           name='lista_complejidad'),
                       url(r'^complejidad/nuevo',
                           views.add_complejidad,
                           name='add_complejidad'),
                       url(r'^complejidad/editar/(?P<pk>\d+)/$',
                           views.edit_complejidad,
                           name='edit_complejidad'),
                       url(r'^complejidad/search',
                           views.search_complejidad,
                           name='search_complejidad'),
                       url(r'^servicio_material/(?P<idserv>\d+)/(?P<idmat>\d+)/$',
                           views.buscar_servicio_material,
                           name='buscar_servicio_material'),
                       url(r'^servicio_material/nuevo/(?P<id_ser>\d+)/$',
                           views.add_serviciomaterial,
                           name='add_serviciomaterial'),
                       url(r'^servicio_material/editar/(?P<pk>\d+)/$',
                           views.edit_serviciomaterial,
                           name='edit_serviciomaterial'),
                       url(r'^complejidad_servicio/(?P<idserv>\d+)/(?P<idcomp>\d+)/$',
                           views.buscar_complejidad_servicio,
                           name='buscar_complejidad_servicio'),
                       url(r'^complejidad_servicio/nuevo/(?P<id_ser>\d+)/',
                           views.add_complejidadservicio,
                           name='add_complejidadservicio'),
                       url(r'^complejidad_servicio/editar/(?P<pk>\d+)/$',
                           views.edit_complejidadservicio,
                           name='edit_complejidadservicio'),
                       url(r'^unidad/$',
                           views.lista_unidad,
                           name='lista_unidad'),
                       url(r'^unidad/nuevo',
                           views.add_unidad,
                           name='add_unidad'),
                       url(r'^unidad/editar/(?P<pk>\d+)/$',
                           views.edit_unidad,
                           name='edit_unidad'),
                       url(r'^unidad/search',
                           views.search_unidad,
                           name='search_unidad'),)
