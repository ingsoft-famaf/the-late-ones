from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^subir_archivo/(?P<pk>[0-9]+)$',
        views.subir_archivo, name='subir_archivo'),
    url(r'^lista_archivo_adj/(?P<pk>[0-9]+)$',
        views.lista_archivos, name='lista_archivos'),
    url(r'^eliminar_archivo/(?P<pk>[0-9]+)$',
        views.eliminar_archivo, name='eliminar_archivo'),
    url(r'^subir_archivo_submeta/(?P<pk>[0-9]+)$',
        views.subir_archivo_submeta, name='subir_archivo_submeta'),
    url(r'^lista_archivo_adj_submeta/(?P<pk>[0-9]+)$',
        views.lista_archivos_submeta, name='lista_archivos_submeta'),
    url(r'^eliminar_archivo_submeta/(?P<pk>[0-9]+)$',
        views.eliminar_archivo_submeta, name='eliminar_archivo_submeta'),
]
