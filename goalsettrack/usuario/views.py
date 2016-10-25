""" Vistas de la aplicación usuario """

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import CreateView



def main_page(request):
    """ Opciones: ir a registrarse o a iniciar sesión """
    template = get_template('main_page.html')
    output = template.render()
    return HttpResponse(output)


class Registro(CreateView):
    """ Automático de Django """
    template_name = 'registro.html'
    form_class = UserCreationForm
    success_url = '/login/'
