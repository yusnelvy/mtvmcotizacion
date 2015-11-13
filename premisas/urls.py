from django.conf.urls import patterns, url
from premisas.views import EmpresaList, EmpresaDetail
from premisas import views

urlpatterns = patterns('',
                       url(r'^$',
                           EmpresaList.as_view(),
                           name='EmpresaDetail'),
                       url(r'^ficha/(?P<pk>\d+)/$',
                           EmpresaDetail.as_view(),
                           name='EmpresaDetail'),)
