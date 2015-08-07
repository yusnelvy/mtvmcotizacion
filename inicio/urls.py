"""
docstring para tipo_clienteurls.py

Pendiente de documentación
"""

from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from inicio import views


urlpatterns = patterns('',
                       url(r'^$', views.pantalla_inicial, name='pantalla_inicial'),
                       url(r'^index/$', views.pantalla_inicial, name='pantalla_inicial'),
                       url(r'^signup$', 'inicio.views.signup', name='signup'),
                       url(r'^login$', login, {'template_name': 'login/login.html', }, name="login"),
                       url(r'^home$', 'inicio.views.home', name='home'),
                       url(r'^logout$', logout, {'template_name': 'base_menu.html', }, name="logout"),)
