from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^subir_archivo/(?P<pk>[0-9]+)$',
        views.subir_archivo, name='subir_archivo'),
    url(r'^lista_archivo_adj/(?P<pk>[0-9]+)$',
        views.lista_archivos, name='lista_archivos'),
]
