from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^crear_comentario/$', views.crear_comentario, name='crear_comentario')
]

