from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import ContactUS, ContactForm
from .forms import ContactFormClass


class ContactUsView(CreateView):
    model = ContactForm
    form_class = ContactFormClass
    success_url = reverse_lazy('contact:page')
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = ContactUS.objects.first()
        return context