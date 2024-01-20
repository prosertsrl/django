from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . models import Prueba


# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/home.html'
    
class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['A','B','C']
    context_object_name = 'lista_prueba'
    
class ModelPruebaListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name = 'prueba'