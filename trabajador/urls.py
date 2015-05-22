from django.conf.urls import patterns, url
from trabajador import views


urlpatterns = patterns('',
                       url(r'^$', views.lista_cargotrabajador, name='lista_cargotrabajador'),
                       url(r'^nuevo', views.add_cargotrabajador, name='add_cargotrabajador'),
                       url(r'^editar/(?P<pk>\d+)/$', views.edit_cargotrabajador,
                           name='edit_cargotrabajador'),
                       )
