from django.conf.urls import patterns, url

from direccion import views

urlpatterns = patterns('',
                       url(r'^$', views.lista_direccion, name='lista_direccion'),
                       url(r'^nuevo', views.add_direccion, name='add_direccion'),
                       url(r'^(?P<pk>\d+)/$', views.edit_direccion, name='edit_direccion'),
                       url(r'^tipo_direccion/$', views.lista_tipo_direccion,
                           name='lista_tipo_direccion'),
                       url(r'^tipo_direccion/nuevo', views.add_tipo_direccion,
                           name='add_tipo_direccion'),
                       url(r'^tipo_direccion/(?P<pk>\d+)/$',
                           views.edit_tipo_direccion, name='edit_tipo_direccion'),
                       url(r'^pais/$', views.lista_pais, name='lista_pais'),
                       url(r'^pais/nuevo', views.add_pais, name='add_pais'),
                       url(r'^pais/(?P<pk>\d+)/$', views.edit_pais,
                           name='edit_pais'),
                       url(r'^provincia/$', views.lista_provincia,
                           name='lista_provincia'),
                       url(r'^provincia/nuevo', views.add_provincia,
                           name='add_provincia'),
                       url(r'^provincia/(?P<pk>\d+)/$', views.edit_provincia,
                           name='edit_provincia'),
                       url(r'^ciudad/$', views.lista_ciudad,
                           name='lista_ciudad'),
                       url(r'^ciudad/nuevo', views.add_ciudad,
                           name='add_ciudad'),
                       url(r'^ciudad/(?P<pk>\d+)/$', views.edit_ciudad,
                           name='edit_ciudad'),
                       url(r'^zona/$', views.lista_zona,
                           name='lista_zona'),
                       url(r'^zona/nuevo', views.add_zona,
                           name='add_zona'),
                       url(r'^zona/(?P<pk>\d+)/$', views.edit_zona,
                           name='edit_zona'),
                       url(r'^lista_tipo_inmueble/$', views.lista_tipo_inmueble,
                           name='lista_tipo_inmueble'),
                       url(r'^lista_tipo_inmueble/nuevo', views.add_tipo_inmueble,
                           name='add_tipo_inmueble'),
                       url(r'^lista_tipo_inmueble/(?P<pk>\d+)/$', views.edit_tipo_inmueble,
                           name='edit_tipo_inmueble'),

                       )
