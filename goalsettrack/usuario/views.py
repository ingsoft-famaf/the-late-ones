# from django.contrib.auth import authenticate, login, logout, views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
# from django.contrib.contenttypes.models import ContentType
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from django.template import Context
# from django.template.context import RequestContext
# from django.template.loader import get_template
# from django.urls import reverse
from django.utils.decorators import method_decorator
# from django.views import generic
from django.views.generic import CreateView, DetailView, UpdateView
# from django.views.generic import ListView, TemplateView

from usuario.forms import FormularioUsuario
from usuario.models import Usuario


def pagina_principal(request):
    """ Donde se elige entre login o registro """

    return render(request, 'pagina_principal.html')


class Registro(CreateView):
    """ Registro de usuario """

    template_name = 'registro.html'
    form_class = UserCreationForm
    success_url = '/login/'


class DetallePerfil(DetailView):
    """ Vista de datos de la cuenta de usuario """

    model = FormularioUsuario
    template_name = 'perfil.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        actual_user = get_object_or_404(User, username=self.request.user)
        return get_object_or_404(Usuario, usuario=actual_user)


class EditarPerfil(UpdateView):
    """ Edición de datos de la cuenta de usuario """

    template_name = 'editar_perfil.html'
    model = Usuario
    form_class = FormularioUsuario
    success_url = '/lista_de_metas/'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        actual_user = get_object_or_404(User, username=self.request.user)
        return get_object_or_404(Usuario, usuario=actual_user)

    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.usuario = User.objects.get(username=self.request.user)
        usuario.save()
        return HttpResponseRedirect(self.get_success_url())
