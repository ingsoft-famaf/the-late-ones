from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^crear_categoria$', views.crear_categoria, name='crear_categoria'),
    url(r'^lista_categorias$', views.lista_categorias, name='lista_categorias')
]

