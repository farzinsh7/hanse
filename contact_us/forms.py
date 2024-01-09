from django import forms
from .models import ContactForm


class ContactFormClass(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'phone', 'message')
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control background-white', 'placeholder':'Your Name', 'type':'text'}),
        'email': forms.EmailInput(attrs={'class': 'form-control background-white', 'placeholder':'Email', 'type':'email'}),
        'phone': forms.TextInput(attrs={'class': 'form-control background-white', 'placeholder':'Phone Number', 'type':'text'}),
        'message': forms.Textarea(attrs={'class': 'form-control background-white', 'placeholder':'Enter your descriptions here...', 'row':'11'}),
        }