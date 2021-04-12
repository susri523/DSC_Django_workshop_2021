from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    '''inherit from generic templateview'''
    template_name = 'helloworld/home.html'
