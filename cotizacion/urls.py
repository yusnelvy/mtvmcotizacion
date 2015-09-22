"""Docstring"""

from django.conf.urls import patterns, url
from cotizacion import views
from cotizacion.views import EstadoCreate


urlpatterns = patterns('',
                       url(r'^$',
                           views.lista_cotizacion,
                           name='lista_cotizacion'),
                       url(r'^nuevo',
                           views.add_cotizacion,
                           name='add_cotizacion'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           views.edit_cotizacion,
                           name='edit_cotizacion'),
                       url(r'^buscar/(?P<pk>\d+)/$',
                           views.buscar_cotizacion,
                           name='buscar_cotizacion'),
                       url(r'^estado_cotizacion/$',
                           views.lista_estado_cotizacion,
                           name='lista_estado_cotizacion'),
                       url(r'^estado_cotizacion/nuevo',
                           views.add_estadocotizacion,
                           name='add_estadocotizacion'),
                       url(r'^estado_cotizacion/nuevo2/$', EstadoCreate.as_view(),
                           name='EstadoCreate'),
                       url(r'^estado_cotizacion/editar/(?P<pk>\d+)/$',
                           views.edit_estadocotizacion,
                           name='edit_estadocotizacion'),
                       url(r'^piso/$',
                           views.lista_piso,
                           name='lista_piso'),
                       url(r'^piso/nuevo',
                           views.add_piso,
                           name='add_piso'),
                       url(r'^piso/editar/(?P<pk>\d+)/$',
                           views.edit_piso,
                           name='edit_piso'),
                       url(r'^tiempo_carga/$',
                           views.lista_tiempocarga,
                           name='lista_tiempocarga'),
                       url(r'^tiempo_carga/nuevo',
                           views.add_tiempocarga,
                           name='add_tiempocarga'),
                       url(r'^tiempo_carga/editar/(?P<pk>\d+)/$',
                           views.edit_tiempocarga,
                           name='edit_tiempocarga'),
                       url(r'^vehiculo/$',
                           views.lista_vehiculo,
                           name='lista_vehiculo'),
                       url(r'^vehiculo/nuevo',
                           views.add_vehiculo,
                           name='add_vehiculo'),
                       url(r'^vehiculo/editar/(?P<pk>\d+)/$',
                           views.edit_vehiculo,
                           name='edit_vehiculo'),
                       url(r'^vehiculo_cotizacion/(?P<idcotizacion>\d+)/$',
                           views.buscar_vehiculocotizacion,
                           name='buscar_vehiculocotizacion'),
                       url(r'^vehiculo_cotizacion/nuevo',
                           views.add_vehiculocotizacion,
                           name='add_vehiculocotizacion'),
                       url(r'^vehiculo_cotizacion/editar/(?P<pk>\d+)/$',
                           views.edit_vehiculocotizacion,
                           name='edit_vehiculocotizacion'),
                       url(r'^cotizacion_direccion/(?P<idcotizacion>\d+)/$',
                           views.buscar_direccioncotizacion,
                           name='buscar_direccioncotizacion'),
                       url(r'^cotizacion_direccion/nuevo/(?P<idcotizacion>\d+)/',
                           views.add_cotizaciondireccion,
                           name='add_cotizaciondireccion'),
                       url(r'^cotizacion_direccion/editar/(?P<pk>\d+)/$',
                           views.edit_cotizaciondireccion,
                           name='edit_cotizaciondireccion'),
                       url(r'^cotizacion_trabajador/(?P<idcotizacion>\d+)/$',
                           views.buscar_cotizaciontrabajador,
                           name='buscar_cotizaciontrabajador'),
                       url(r'^cotizacion_trabajador/nuevo/(?P<idcotizacion>\d+)/',
                           views.add_cotizaciontrabajador,
                           name='add_cotizaciontrabajador'),
                       url(r'^cotizacion_trabajador/editar/(?P<pk>\d+)/$',
                           views.edit_cotizaciontrabajador,
                           name='edit_cotizaciontrabajador'),
                       url(r'^cotizacion_ambiente/(?P<idcotizacion>\d+)/$',
                           views.buscar_cotizacionambiente,
                           name='buscar_cotizacionambiente'),
                       url(r'^cotizacion_ambiente/nuevo/(?P<idcotizacion>\d+)/',
                           views.add_cotizacionambiente,
                           name='add_cotizacionambiente'),
                       url(r'^cotizacion_ambiente/editar/(?P<pk>\d+)/$',
                           views.edit_cotizacionambiente,
                           name='edit_cotizacionambiente'),
                       url(r'^cotizacion_mueble/(?P<idcotizacionambiente>\d+)/$',
                           views.buscar_cotizacionmueble,
                           name='buscar_cotizacionmueble'),
                       url(r'^cotizacion_mueble/nuevo/(?P<idcotizacionambiente>\d+)/',
                           views.add_cotizacionmueble,
                           name='add_cotizacionmueble'),
                       url(r'^cotizacion_mueble/editar/(?P<pk>\d+)/$',
                           views.edit_cotizacionmueble,
                           name='edit_cotizacionmueble'),
                       url(r'^cotizacion_servicio/(?P<idcotizacionmueble>\d+)/$',
                           views.buscar_cotizacionservicio,
                           name='buscar_cotizacionservicio'),
                       url(r'^cotizacion_servicio/nuevo/(?P<idcotizacionmueble>\d+)/$',
                           views.add_cotizacionservicio,
                           name='add_cotizacionservicio'),
                       url(r'^cotizacion_servicio/nuevo/(?P<idcotizacionmueble>\d+) \
                           /(?P<idcotizacioncontenido>\d+)/$',
                           views.add_cotizacionservicio,
                           name='add_cotizacionservicio'),
                       url(r'^cotizacion_servicio/editar/(?P<pk>\d+)/$',
                           views.edit_cotizacionservicio,
                           name='edit_cotizacionservicio'),
                       url(r'^cotizacion_material/(?P<idcotizacionservicio>\d+)/$',
                           views.buscar_cotizacionmaterial,
                           name='buscar_cotizacionmaterial'),
                       url(r'^cotizacion_material/nuevo/(?P<idcotizacionservicio>\d+)/$',
                           views.add_cotizacionmaterial,
                           name='add_cotizacionmaterial'),
                       url(r'^cotizacion_material/editar/(?P<pk>\d+)/$',
                           views.edit_cotizacionmaterial,
                           name='edit_cotizacionmaterial'),
                       url(r'^cotizacion_contenido/(?P<idcotizacionmueble>\d+)/$',
                           views.buscar_cotizacioncontenido,
                           name='buscar_cotizacioncontenido'),
                       url(r'^cotizacion_contenido/nuevo',
                           views.add_cotizacioncontenido,
                           name='add_cotizacioncontenido'),
                       url(r'^cotizacion_contenido/editar/(?P<pk>\d+)/$',
                           views.edit_cotizacioncontenido,
                           name='edit_cotizacioncontenido'),
                       url(r'^cotizacion_material/nuevo/(?P<idcotizacionservicio>\d+)/cargar/$',
                           views.cargar_datos_material,
                           name='cargar_datos_material'),)
