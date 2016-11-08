from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^crear_recordatorio/(?P<pk>[0-9]+)$', views.crear_recordatorio, name='crear_recordatorio'),
    url(r'^lista_recordatorio_meta/(?P<pk>[0-9]+)$', views.lista_recordatorio_meta, name='lista_recordatorio_meta'),
    url(r'^lista_recordatorio_meta/eliminar_recordatorio/(?P<pk>[0-9]+)$', views.eliminar_recordatorio, name='eliminar_recordatorio'),
    url(r'^lista_recordatorio_meta/editar_recordatorio/(?P<pk>[0-9]+)$', views.editar_recordatorio, name='editar_recordatorio'),
    url(r'^lista_recordatorio_meta/info_recordatorio/(?P<pk>[0-9]+)$', views.info_recordatorio, name='info_recordatorio'),
    url(r'^lista_recordatorio_meta/eliminar_recordatorios_viejos/(?P<pk>[0-9]+)$', views.eliminar_recordatorios_viejos, name='eliminar_recordatorios_viejos'),
]
