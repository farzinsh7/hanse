from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import ContactUS, ContactForm
from django.http import HttpResponse


class ContactUsView(ListView):
    model = ContactForm
    template_name = 'contact.html'
    context_object_name = 'contact'
    queryset = ContactUS.objects.first()

def add_form(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    form = ContactForm.objects.create(name=name, email=email, phone=phone, message=message)
    return HttpResponse("<h5 class='color-success' >Your message has been successfully sent.</h5>")