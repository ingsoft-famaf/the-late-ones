from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views
from django.contrib.auth.views import logout


urlpatterns = [
    # pagina principal
    url(r'^$', views.main_page, name='/'),
    # pagina de login
    url(r'^$/login/', TemplateView.as_view(template_name='login.html')),
    # pagina de logout
    url(r'^logout$', logout, name="logout"),
    # pagina de registro
    url(r'^registro', views.Registro.as_view(), name='registro'),
]
