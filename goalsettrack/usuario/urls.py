from django.conf.urls import url

from . import views

urlpatterns = [
    # pagina principal
    url(r'^$', views.main_page, name=''),
    # pagina de registro
    url(r'^$', views.pagina_registro, name='registro'),
]
