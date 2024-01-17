from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import ContactUS, ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail


class ContactUsView(ListView):
    model = ContactForm
    template_name = 'contact.html'
    context_object_name = 'contact'
    queryset = ContactUS.objects.first()

def add_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        form = ContactForm.objects.create(name=name, email=email, phone=phone, message=message)

        # Send email notification to admin
        subject = 'New Form Submission'
        email_message = f"A new form submission:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        from_email = 'hanse.trading@htg-hanse-trading.de'  # Replace with your email
        recipient_list = ['eg.styleofficial@gmail.com']  # Replace with your admin email address
        send_mail(subject, email_message, from_email, recipient_list, fail_silently=False)

        return HttpResponse("<h5 class='color-success'>Your message has been successfully sent.</h5>")

    return HttpResponse("Invalid request method")