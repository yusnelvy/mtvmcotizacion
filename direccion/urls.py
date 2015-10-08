"""Docstring"""

from django.conf.urls import patterns, url
from direccion import views

urlpatterns = patterns('',
                       url(r'^$',
                           views.lista_direccion,
                           name='lista_direccion'),
                       url(r'^nuevo/(?P<id_cli>\d+)/',
                           views.add_direccion,
                           name='add_direccion'),
                       url(r'^(?P<pk>\d+)/$',
                           views.edit_direccion,
                           name='edit_direccion'),
                       url(r'^tipo_direccion/$',
                           views.lista_tipo_direccion,
                           name='lista_tipo_direccion'),
                       url(r'^tipo_direccion/nuevo',
                           views.add_tipo_direccion,
                           name='add_tipo_direccion'),
                       url(r'^tipo_direccion/(?P<pk>\d+)/$',
                           views.edit_tipo_direccion,
                           name='edit_tipo_direccion'),
                       url(r'^tipo_direccion/search_tipo_direccion/$',
                           views.search_tipo_direccion,
                           name='search_tipo_direccion'),
                       url(r'^pais/$',
                           views.lista_pais,
                           name='lista_pais'),
                       url(r'^pais/nuevo',
                           views.add_pais,
                           name='add_pais'),
                       url(r'^pais/editar/(?P<pk>\d+)$',
                           views.edit_pais,
                           name='edit_pais'),
                       url(r'^pais/search_pais/$',
                           views.search_pais,
                           name='search_pais'),
                       url(r'^provincia/$',
                           views.lista_provincia,
                           name='lista_provincia'),
                       url(r'^provincia/nuevo',
                           views.add_provincia,
                           name='add_provincia'),
                       url(r'^provincia/(?P<pk>\d+)/$',
                           views.edit_provincia,
                           name='edit_provincia'),
                       url(r'^provincia/search_provincia/$',
                           views.search_provincia,
                           name='search_provincia'),
                       url(r'^ciudad/$',
                           views.lista_ciudad,
                           name='lista_ciudad'),
                       url(r'^ciudad/nuevo',
                           views.add_ciudad,
                           name='add_ciudad'),
                       url(r'^ciudad/(?P<pk>\d+)/$',
                           views.edit_ciudad,
                           name='edit_ciudad'),
                       url(r'^ciudad/search_ciudad/$',
                           views.search_ciudad,
                           name='search_ciudad'),
                       url(r'^zona/$',
                           views.lista_zona,
                           name='lista_zona'),
                       url(r'^zona/nuevo',
                           views.add_zona,
                           name='add_zona'),
                       url(r'^zona/(?P<pk>\d+)/$',
                           views.edit_zona,
                           name='edit_zona'),
                       url(r'^zona/search_zona/$',
                           views.search_zona,
                           name='search_zona'),
                       url(r'^tipo_inmueble/$',
                           views.lista_tipo_inmueble,
                           name='lista_tipo_inmueble'),
                       url(r'^tipo_inmueble/nuevo',
                           views.add_tipo_inmueble,
                           name='add_tipo_inmueble'),
                       url(r'^tipo_inmueble/(?P<pk>\d+)/$',
                           views.edit_tipo_inmueble,
                           name='edit_tipo_inmueble'),
                       url(r'^tipo_inmueble/search_tipo_inmueble/$',
                           views.search_tipo_inmueble,
                           name='search_tipo_inmueble'),
                       url(r'^complejidad_inmueble/$',
                           views.lista_complejidad_inmueble,
                           name='lista_complejidad_inmueble'),
                       url(r'^complejidad_inmueble/nuevo',
                           views.add_complejidad_inmueble,
                           name='add_complejidad_inmueble'),
                       url(r'^complejidad_inmueble/(?P<pk>\d+)/$',
                           views.edit_complejidad_inmueble,
                           name='edit_complejidad_inmueble'),
                       url(r'^complejidad_inmueble/search_complejidad_inmueble/$',
                           views.search_complejidad_inmueble,
                           name='search_complejidad_inmueble'),
                       url(r'^inmueble/(?P<iddireccion>\d+)/$',
                           views.lista_inmueble,
                           name='lista_inmueble'),
                       url(r'^inmueble/nuevo',
                           views.add_inmueble,
                           name='add_inmueble'),
                       url(r'^inmueble/editar/(?P<pk>\d+)/$',
                           views.edit_inmueble,
                           name='edit_inmueble'))
