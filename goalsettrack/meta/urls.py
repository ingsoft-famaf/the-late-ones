from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.crear_meta, name='crear_meta'),
]
