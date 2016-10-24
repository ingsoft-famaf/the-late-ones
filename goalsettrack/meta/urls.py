from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^lista_de_metas/$', views.lista_de_metas, name='lista_de_metas'),
    url(r'^lista_de_metas/crear_meta/$', views.crear_meta, name='crear_meta'),
]
