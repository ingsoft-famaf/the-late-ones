from django.shortcuts import render, render_to_response
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import Context
from django.template.loader import get_template
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import views
from django.views.generic import CreateView, UpdateView, ListView
from django.views.generic import DetailView, TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from usuario.forms import *
from django.template.context import RequestContext

def main_page(request):
    template = get_template('main_page.html')
    output = template.render()
    return HttpResponse(output)

class Registro(CreateView):

    template_name = 'registro.html'
    form_class = UserCreationForm
    success_url = '/login/'

class DetallePerfil(DetailView):

    model = FormularioUsuario
    template_name = 'perfil.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):

        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_object(self):

        ActualUser = get_object_or_404(User, username=self.request.user)
        return get_object_or_404(Usuario, usuario=ActualUser)


class EditarPerfil(UpdateView):

    template_name = 'editar_perfil.html'
    model = Usuario
    form_class = FormularioUsuario
    success_url = '/lista_de_metas/'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):

        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_object(self):

        ActualUser = get_object_or_404(User, username=self.request.user)
        return get_object_or_404(Usuario, usuario=ActualUser)

    def form_valid(self, form):

        usuario = form.save(commit=False)
        usuario.usuario = User.objects.get(username=self.request.user)
        usuario.save()
        return HttpResponseRedirect(self.get_success_url())

def lista_de_metas(request):
    template = get_template('lista_de_metas.html')
    output = template.render()
    return HttpResponse(output)

