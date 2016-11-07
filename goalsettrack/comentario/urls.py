from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^crear_comentario/(?P<pk>[0-9]+)$',
        views.crear_comentario, name='crear_comentario'),
    url(r'^lista_comentarios/(?P<pk>[0-9]+)$',
        views.lista_comentarios, name='lista_comentarios'),
    url(r'^eliminar_comentario/(?P<pk>[0-9]+)$',
        views.eliminar_comentario, name='eliminar_comentario'),
    url(r'^editar_comentario/(?P<pk>[0-9]+)$',
        views.editar_comentario, name='editar_comentario'),
    url(r'^crear_comentario_submeta/(?P<pk>[0-9]+)$',
        views.crear_comentario_submeta, name='crear_comentario_submeta'),
    url(r'^eliminar_comentario_submeta/(?P<pk>[0-9]+)$',
        views.eliminar_comentario_submeta, name='eliminar_comentario_submeta'),
    url(r'^editar_comentario_submeta/(?P<pk>[0-9]+)$',
        views.editar_comentario_submeta, name='editar_comentario_submeta'),
    url(r'^lista_comentarios_submeta/(?P<pk>[0-9]+)$',
        views.lista_comentarios_submeta, name='lista_comentarios_submeta')
]
