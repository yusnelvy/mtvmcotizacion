from django.conf.urls import patterns, url

from cliente import views

urlpatterns = patterns('',
                       url(r'^$', views.lista_cliente, name='lista_cliente'),
                       url(r'^nuevo', views.add_cliente, name='add_cliente'),
                       url(r'^editar/(?P<pk>\d+)/$', views.edit_cliente, name='edit_cliente'),
                       url(r'^email/(?P<id_cli>\d+)/$', views.lista_email, name='lista_email'),
                       url(r'^email/nuevo$', views.add_email, name='add_email'),
                       url(r'^sexo/$', views.lista_sexo, name='lista_sexo'),
                       url(r'^sexo/nuevo/$', views.add_sexo, name='add_sexo'),
                       url(r'^estado_civil/$', views.lista_estadocivil, name='lista_estadocivil'),
                       url(r'^estado_civil/nuevo/$', views.add_estadocivil, name='add_estadocivil'),
                       url(r'^cliente_ficha/(?P<id_cli>\d+)/email/editar/(?P<pk>\d+)/$',
                           views.edit_email, name='edit_email'),
                       url(r'^telefono/(?P<id_cli>\d+)/$', views.lista_telefono_cliente,
                           name='lista_telefono_cliente'),
                       url(r'^direccion/(?P<id_cli>\d+)/$', views.lista_direccioncliente,
                           name='lista_direccioncliente'),
                       url(r'^cliente_ficha/(?P<pk>\d+)/$', views.ficha_cliente,
                           name='ficha_cliente'),

                       )
