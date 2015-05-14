from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mtvmcotizacion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^direccion/', include('direccion.urls', namespace="udireciones")),
    url(r'^telefono/', include('telefono.urls', namespace="utelefonos")),
)

# se agrego para probar los estilo
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.STATICFILES_DIRS}),
    )
