from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^lista_de_metas/$', views.lista_de_metas, name='lista_de_metas'),
    url(r'^lista_de_metas/progreso_mensual/$', views.progreso_mensual, name='progreso_mensual'),
    url(r'^notificaciones/$', views.notificaciones, name='notificaciones'),
    url(r'^recordatorio_instantaneo/$', views.recordatorio_instantaneo, name='recordatorio_instantaneo'),
    url(r'^lista_de_metas/crear_meta/$', views.crear_meta, name='crear_meta'),
    url(r'^lista_de_metas/info_meta/(?P<pk>[0-9]+)/$', views.info_meta,
        name='info_meta'),
    url(r'^lista_de_metas/editar_meta/(?P<pk>[0-9]+)$', views.editar_meta,
        name='editar_meta'),
    url(r'^lista_de_metas/eliminar_meta/(?P<pk>[0-9]+)/$', views.eliminar_meta,
        name='eliminar_meta'),
    url(r'^lista_de_metas/filtrar_meta$',
        views.filtrar_meta, name='filtrar_meta'),
    url(r'^lista_de_metas/info_meta/lista_de_submetas/(?P<pk>[0-9]+)/$',
        views.lista_de_submetas, name='lista_de_submetas'),
    url(r'^lista_de_metas/info_meta/lista_de_submetas/crear_submeta/(?P<pk>[0-9]+)/$',
        views.crear_submeta, name='crear_submeta'),
    url(r'^lista_de_metas/info_meta/lista_de_submetas/info_submeta/(?P<pk>[0-9]+)/$',
        views.info_submeta, name='info_submeta'),
    url(r'^lista_de_metas/info_meta/lista_de_submetas/editar_submeta/(?P<pk>[0-9]+)$',
        views.editar_submeta, name='editar_submeta'),
    url(r'^lista_de_metas/info_meta/lista_de_submetas/eliminar_submeta/(?P<pk>[0-9]+)$',
        views.eliminar_submeta, name='eliminar_submeta'),
    url(r'^ver_notificaciones/$', views.ver_notificaciones, name='ver_notificaciones'),
]
