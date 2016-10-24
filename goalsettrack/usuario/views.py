from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import Context
from django.template.loader import get_template

def main_page(request):
    template = get_template('main_page.html')
    output = template.render()
    return HttpResponse(output)
