from django.conf.urls import patterns, url
from contenido import views


urlpatterns = patterns('',
                       url(r'^$', views.lista_contenido, name='lista_contenido'),
                       url(r'^nuevo', views.add_contenido, name='add_contenido'),
                       url(r'^editar/(?P<pk>\d+)/$', views.edit_contenido,
                           name='edit_contenido'),
                       url(r'^contenido_tipico/(?P<idmueble>\d+)/$',
                           views.buscar_contenidotipico,
                           name='buscar_contenidotipico'),
                       url(r'^contenido_tipico/nuevo/$', views.add_contenidotipico,
                           name='add_contenidotipico'),
                       url(r'^contenido_tipico/editar/(?P<pk>\d+)/$',
                           views.edit_contenidotipico,
                           name='edit_contenidotipico'),
                       url(r'^contenido_servicio/(?P<idservicio>\d+)/$',
                           views.buscar_contenidoservicio,
                           name='buscar_contenidoservicio'),
                       url(r'^contenido_servicio/nuevo/$', views.add_contenidoservicio,
                           name='add_contenidoservicio'),
                       url(r'^contenido_servicio/editar/(?P<pk>\d+)/$',
                           views.edit_contenidoservicio,
                           name='edit_contenidoservicio'),

                       )
