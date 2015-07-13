from django.conf.urls import patterns, url
from telefono import views


urlpatterns = patterns('',
                       url(r'^$', views.lista_telefono, name='lista_telefono'),
                       url(r'^nuevo/(?P<id_cli>\d+)/', views.add_telefono, name='add_telefono'),
                       url(r'^editar/(?P<pk>\d+)/$', views.edit_telefono,
                           name='edit_telefono'),
                       url(r'^tipo_telefono/$', views.lista_tipotelefono,
                           name='lista_tipotelefono'),
                       url(r'^tipo_telefono/nuevo', views.add_tipotelefono,
                           name='add_tipotelefono'),
                       url(r'^tipo_telefono/editar/(?P<pk>\d+)/$',
                           views.edit_tipotelefono, name='edit_tipotelefono'),
                       )
