from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from django import forms

# Create your views here.


class Hogar(TemplateView):
    template_name="hogar.html"


class Registrar():
    template_name="registrar.html"


class Lista(View):
    template_name="lista.html"


class Estadistica():
    template_name="estadistica.html"
