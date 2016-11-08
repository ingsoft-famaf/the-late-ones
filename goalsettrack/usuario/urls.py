from django.conf.urls import url
from django.contrib.auth.views import logout
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.pagina_principal, name='/'),
    url(r'^$/login/', TemplateView.as_view(template_name='login.html')),
    url(r'^logout$', logout, name="logout"),
    url(r'^registro', views.Registro.as_view(), name='registro'),
    url(r'^perfil/', views.DetallePerfil.as_view(), name='perfil'),
    url(r'^editar_perfil', views.EditarPerfil.as_view(),
        name='editar_perfil'),
]
