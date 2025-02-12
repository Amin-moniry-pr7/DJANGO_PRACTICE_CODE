# from django.shortcuts import render
# from django.views.generic import TemplateView

from django.views.generic import ListView
from .models import ab

class PMRESPONDE(ListView):
    model = ab
    template_name = 'S_D.html'
