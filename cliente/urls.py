from django.conf.urls import patterns, url

from cliente import views


urlpatterns = patterns('',
    url(r'^$', views.lista_cliente, name='lista_cliente'),
    url(r'^nuevo', views.add_cliente, name='add_cliente'),
    url(r'^editar', views.edit_cliente, name='edit_cliente'),
    url(r'^email/$', views.lista_email, name='lista_email'),
    url(r'^email/nuevo$', views.add_email, name='add_email'),
    url(r'^email/(?P<id_cli>\d+)/editar/(?P<pk>\d+)/$', views.edit_email, name='edit_email'),
    url(r'^telefono/(?P<id_cli>\d+)/$', views.lista_telefono_cliente,
        name='lista_telefono_cliente'),
    url(r'^direccion/(?P<id_cli>\d+)/$', views.lista_direccioncliente,
        name='lista_direccioncliente'),

    )
