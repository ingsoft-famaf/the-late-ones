""" Parseo de urls de la app usuario """

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth.views import logout
from . import views


urlpatterns = [
    url(r'^$', views.main_page, name='/'),
    url(r'^login$', TemplateView.as_view(template_name='login.html')),
    url(r'^logout$', logout, name="logout"),
    url(r'^registro', views.Registro.as_view(), name='registro'),
]
