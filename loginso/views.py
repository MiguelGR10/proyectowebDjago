from django.shortcuts import render
from django.views.generic import TemplateView


class login(TemplateView):
    template_name = 'login.html'
