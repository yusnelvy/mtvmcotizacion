"""
Docstring pendiente para este documento
"""

from django.conf.urls import patterns, url
from gestiondocumento.views import EstadoList, EstadoDocumentoList,\
    EstadoView, EstadoDocumentoView, EstadoUpdate,\
    EstadoDocumentoUpdate, EstadoDelete, EstadoDocumentoDelete
from gestiondocumento import views

urlpatterns = patterns('',
                       url(r'^$',
                           EstadoList.as_view(),
                           name='EstadoList'),
                       url(r'^nuevo',
                           EstadoView.as_view(),
                           name='EstadoView'),
                       url(r'^editar/(?P<pk>\d+)/$',
                           EstadoUpdate.as_view(),
                           name='EstadoUpdate'),
                       url(r'^search',
                           views.search_estado,
                           name='search_estado'),
                       url(r'^delete/(?P<pk>\d+)/$',
                           EstadoDelete.as_view(),
                           name='EstadoDelete'),
                       url(r'^estadodocumento/$',
                           EstadoDocumentoList.as_view(),
                           name='EstadoDocumentoList'),
                       url(r'^estadodocumento/nuevo',
                           EstadoDocumentoView.as_view(),
                           name='EstadoDocumentoView'),
                       url(r'^estadodocumento/editar/(?P<pk>\d+)/$',
                           EstadoDocumentoUpdate.as_view(),
                           name='EstadoDocumentoUpdate'),
                       url(r'^estadodocumento/search',
                           views.search_estadodocumento,
                           name='search_estadodocumento'),
                       url(r'^estadodocumento/delete/(?P<pk>\d+)/$',
                           EstadoDocumentoDelete.as_view(),
                           name='EstadoDocumentoDelete'),)
