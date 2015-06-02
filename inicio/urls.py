"""
docstring para inicio/urls.py

Pendiente de documentación
"""

from django.conf.urls import patterns, url

from inicio import views

urlpatterns = patterns('',
                       url(r'^$', views.pantalla_inicial, name='pantalla_inicial'),)
