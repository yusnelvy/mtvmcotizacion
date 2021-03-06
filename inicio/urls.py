"""
docstring para tipo_clienteurls.py

Pendiente de documentación
"""

from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from inicio import views
from django.views.generic import TemplateView


urlpatterns = patterns('',
                       url(r'^$',
                           views.pantalla_inicial,
                           name='pantalla_inicial'),
                       url(r'^guiadeestilos/',
                           TemplateView.as_view(template_name="guiaDeEstilos.html"),
                           name='guia_de_estilos'),
                       url(r'^home$',
                           'inicio.views.home',
                           name='home'),
                       url(r'^index/$',
                           views.pantalla_inicial,
                           name='pantalla_inicial'),
                       url(r'^login$',
                           login,
                           {'template_name': 'login.html', },
                           name="login"),
                       url(r'^logout$',
                           logout,
                           {'template_name': 'base_menu.html', },
                           name="logout"),
                       url(r'^signup$',
                           'inicio.views.signup',
                           name='signup'),)
