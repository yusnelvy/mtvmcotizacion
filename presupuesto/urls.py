from django.conf.urls import patterns, url
from presupuesto.views import PresupuestoView, PresupuestoList, PresupuestoDetail, \
    PresupuestoDireccionView, PresupuestoDetalleView, PresupuestoDireccionUpdate, \
    PresupuestoDetalleUpdate, PresupuestoUpdate
from presupuesto import views


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
                       url(r'^detalle/(?P<pk>\d+)/$', views.PresupuestoDetalleUpdate,
                           name='PresupuestoDetalleUpdate'),
                       )
