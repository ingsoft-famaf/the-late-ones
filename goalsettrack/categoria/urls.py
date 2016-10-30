from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^crear_categoria/$', views.crear_categoria, name='crear_categoria'),
    url(r'^detalle_categoria/$', views.detalle_categoria, name='detalle_categoria')
]
