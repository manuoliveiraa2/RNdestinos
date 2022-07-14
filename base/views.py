#from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'
    
#def index(request):
 #   return HttpResponse("Olá, galerinha! Essa é a minha primeira view :)")
