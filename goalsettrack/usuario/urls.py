from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', views.pagina_principal, name='/'),
    url(r'^$/login/', TemplateView.as_view(template_name='login.html')),
    url(r'^logout$', logout, name="logout"),
    url(r'^registro', views.Registro.as_view(), name='registro'),
    url(r'^editar_perfil/', views.EditarPerfil.as_view(), name='editar_perfil'),
    url(r'^perfil/', views.DetallePerfil.as_view(), name='perfil'),
]
