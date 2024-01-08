from django.shortcuts import render
from django.views.generic import ListView
from .models import ContactUS

#Create your views here.
class ContactUsView(ListView):
    model = ContactUS
    queryset = ContactUS.objects.first()
    template_name = 'contact.html'
    context_object_name = "contact"