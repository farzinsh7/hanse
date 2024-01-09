from django.shortcuts import render
from django.views.generic import DetailView
from .models import Investment



class InvestmentLineView(DetailView):
    model = Investment
    context_object_name = 'investment'
    queryset = Investment.objects.published()
    template_name = 'investment_line.html'