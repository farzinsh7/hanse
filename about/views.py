from django.shortcuts import render
from django.views.generic import ListView
from .models import AboutCompany

#Create your views here.
class AboutView(ListView):
    model = AboutCompany
    queryset = AboutCompany.objects.first()
    template_name = 'about.html'
    context_object_name = "about"