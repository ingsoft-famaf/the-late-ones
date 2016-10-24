from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import Context
from django.template.loader import get_template
from .forms import ProfileForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import views
from django.views.generic import CreateView, UpdateView, ListView
from django.views.generic import DetailView, TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm

def main_page(request):
    template = get_template('main_page.html')
    output = template.render()
    return HttpResponse(output)

class Registro(CreateView):
    """
    Vista de registro de usuario para uso de django. Posee la funcionalidad
    de crear nuevos usuarios con sus passwords. Hereda de
    django.views.generic.CreateView
    """
    template_name = 'registro.html'
    form_class = UserCreationForm
    success_url = '/login/'
