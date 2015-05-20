from django.conf.urls import patterns, url
from ambiente import views


urlpatterns = patterns('',
                       url(r'^$', views.lista_ambiente, name='lista_ambiente'),
                       url(r'^buscar/(?P<id_tipoinmueble>\d+)/$', views.buscar_ambiente,
                           name='buscar_ambiente'),
                       url(r'^nuevo', views.add_ambiente, name='add_ambiente'),
                       url(r'^editar/(?P<pk>\d+)/$', views.edit_ambiente,
                           name='edit_ambiente'),
                       url(r'^tipo_ambiente/$', views.lista_tipo_ambiente,
                           name='lista_tipo_ambiente'),
                       url(r'^tipo_ambiente/nuevo', views.add_tipo_ambiente,
                           name='add_tipo_ambiente'),
                       url(r'^tipo_ambiente/editar/(?P<pk>\d+)/$',
                           views.edit_tipo_ambiente, name='edit_tipo_ambiente'),
                       url(r'^tipo_ambientetipoinmueble/$', views.lista_ambiente_tipo_inmueble,
                           name='lista_ambiente_tipo_inmueble'),
                       url(r'^tipo_ambientetipoinmueble/nuevo', views.add_ambiente_tipoinmueble,
                           name='add_ambiente_tipoinmueble'),
                       url(r'^tipo_ambientetipoinmueble/editar/(?P<pk>\d+)/$',
                           views.edit_ambiente_tipoinmueble, name='edit_ambiente_tipoinmueble'),

                       )
