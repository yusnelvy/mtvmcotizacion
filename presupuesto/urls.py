from django.conf.urls import patterns, url
from presupuesto.views import PresupuestoView, PresupuestoList, PresupuestoDetail, \
    PresupuestoDireccionView, PresupuestoDetalleView, PresupuestoDireccionUpdate, \
    PresupuestoDetalleUpdate, PresupuestoUpdate, ContactWizard
from presupuesto import views
from presupuesto.forms import PresupuestoDetalleForm1, PresupuestoDetalleForm2, \
    PresupuestoDetalleForm3


urlpatterns = patterns('',
                       url(r'^$', PresupuestoList.as_view(), name='PresupuestoList'),
                       url(r'^nuevo', PresupuestoView.as_view(), name='PresupuestoView'),
                       url(r'^(?P<pk>\d+)/$', PresupuestoUpdate.as_view(), name='PresupuestoUpdate'),
                       url(r'^ficha/(?P<pk>\d+)/$', PresupuestoDetail.as_view(), name='PresupuestoDetail'),
                       url(r'^direccion/nuevo/', PresupuestoDireccionView.as_view(),
                           name='PresupuestoDireccionView'),
                       url(r'^direccion/(?P<pk>\d+)/$', PresupuestoDireccionUpdate.as_view(),
                           name='PresupuestoDireccionUpdate'),
                       url(r'^detalle/nuevo', PresupuestoDetalleView.as_view(),
                           name='PresupuestoDetalleView'),
                       url(r'^detalle/(?P<pk>\d+)/$', PresupuestoDetalleUpdate.as_view(),
                           name='PresupuestoDetalleUpdate'),
                       url(r'^ajax_tamano_request/$', views.ajax_tamano_request,
                           name='ajax_tamano_request'),
                       url(r'^detalle/$', ContactWizard.as_view([PresupuestoDetalleForm1, PresupuestoDetalleForm2, PresupuestoDetalleForm3])),

                       )
