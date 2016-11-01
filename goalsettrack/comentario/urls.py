from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^crear_comentario/(?P<pk>[0-9]+)$',
        views.crear_comentario, name='crear_comentario'),
    url(r'^detalle_comentario/(?P<pk>[0-9]+)$',
        views.detalle_comentario, name='detalle_comentario'),
    url(r'^lista_comentarios/(?P<pk>[0-9]+)$',
        views.lista_comentarios, name='lista_comentarios')
]
