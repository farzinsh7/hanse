from django import forms
from .models import Subscriber


class NewsLetterFormClass(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email', )
        widgets = {
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Enter Email Here', 'type':'email'}),
        }
