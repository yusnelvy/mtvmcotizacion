from django.conf.urls import patterns, url
from presupuesto.views import PresupuestoView, PresupuestoList, PresupuestoDetail, \
    PresupuestoDireccionView, PresupuestoDetalleView, PresupuestoDireccionUpdate, \
    PresupuestoDetalleUpdate, PresupuestoUpdate, ContactWizard, PresupuestoServicioView, \
    PresupuestoServicioViewFomset, PresupuestoServicioUpdate, PresupuestoDetalleList, \
    PresupuestoDetalleDetail, PresupuestoDetailResumen, PresupuestoDireccionDelete, \
    PresupuestoDelete, PresupuestoDetalleDelete, PresupuestoServicioDelete, \
    PresupuestoServicioList, PresupuestoDetalleServicioDetail, \
    PresupuestoDetalleDetail2, PresupuestoDireccionOrigenDetail, \
    PresupuestoDireccionDestinoDetail, PresupuestoDatosPersonales
from presupuesto import views
from presupuesto.forms import PresupuestoDetalleForm1, PresupuestoDetalleForm2, \
    PresupuestoDetalleForm3


urlpatterns = patterns('',
                       url(r'^$', PresupuestoList.as_view(), name='PresupuestoList'),
                       url(r'^nuevo', PresupuestoView.as_view(), name='PresupuestoView'),
                       url(r'^editar/(?P<pk>\d+)/$', PresupuestoUpdate.as_view(), name='PresupuestoUpdate'),
                       url(r'^ficha/(?P<pk>\d+)/$', PresupuestoDetail.as_view(), name='PresupuestoDetail'),
                       url(r'^ficha/(?P<pk>\d+)/delete/$', PresupuestoDelete.as_view(),
                           name='PresupuestoDelete'),
                       url(r'^ficha/resumen/(?P<pk>\d+)/$', PresupuestoDetailResumen.as_view(),
                           name='PresupuestoDetailResumen'),
                       url(r'^ficha/datospersonales/(?P<pk>\d+)/$', PresupuestoDatosPersonales.as_view(),
                           name='PresupuestoDatosPersonales'),
                       url(r'^ficha/direccionorigen/(?P<pk>\d+)/$', PresupuestoDireccionOrigenDetail.as_view(),
                           name='PresupuestoDireccionOrigenDetail'),
                       url(r'^ficha/direcciondestino/(?P<pk>\d+)/$', PresupuestoDireccionDestinoDetail.as_view(),
                           name='PresupuestoDireccionDestinoDetail'),
                       url(r'^ficha/detalle/(?P<pk>\d+)/$', PresupuestoDetalleDetail2.as_view(),
                           name='PresupuestoDetalleDetail2'),
                       url(r'^direccion/nuevo/', PresupuestoDireccionView.as_view(),
                           name='PresupuestoDireccionView'),
                       url(r'^direccion/(?P<pk>\d+)/$', PresupuestoDireccionUpdate.as_view(),
                           name='PresupuestoDireccionUpdate'),
                       url(r'^direccion/(?P<pk>\d+)/delete/$', PresupuestoDireccionDelete.as_view(),
                           name='PresupuestoDireccionDelete'),
                       url(r'^detalle/$', PresupuestoDetalleList.as_view(),
                           name='PresupuestoDetalleList'),
                       url(r'^detalle/ficha/(?P<pk>\d+)/$', PresupuestoDetalleDetail.as_view(),
                           name='PresupuestoDetalleDetail'),
                       url(r'^detalle/nuevo', PresupuestoDetalleView.as_view(),
                           name='PresupuestoDetalleView'),
                       url(r'^detalle/(?P<pk>\d+)/$', PresupuestoDetalleUpdate.as_view(),
                           name='PresupuestoDetalleUpdate'),
                       url(r'^detalle/(?P<pk>\d+)/delete/$', PresupuestoDetalleDelete.as_view(),
                           name='PresupuestoDetalleDelete'),
                       url(r'^detalle/servicio/(?P<pk>\d+)/$', PresupuestoDetalleServicioDetail.as_view(),
                           name='PresupuestoDetalleServicioDetail'),
                       url(r'^ajax_tamano_request/$', views.ajax_tamano_request,
                           name='ajax_tamano_request'),
                       url(r'^detalle/form$', ContactWizard.as_view([PresupuestoDetalleForm1, PresupuestoDetalleForm2, PresupuestoDetalleForm3])),
                       url(r'^servicio/(?P<pk>\d+)$', PresupuestoServicioList.as_view(),
                           name='PresupuestoServicioList'),
                       url(r'^servicio/nuevo', PresupuestoServicioView.as_view(),
                           name='PresupuestoServicioView'),
                       url(r'^servicio/(?P<pk>\d+)/$', PresupuestoServicioUpdate.as_view(),
                           name='PresupuestoServicioUpdate'),
                       url(r'^servicio/(?P<pk>\d+)/delete/$', PresupuestoServicioDelete.as_view(),
                           name='PresupuestoServicioDelete'),
                       url(r'^servicio/nuevo2', PresupuestoServicioViewFomset.as_view(),
                           name='PresupuestoServicioViewFomset'),
                       )
