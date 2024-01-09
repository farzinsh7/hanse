from django.shortcuts import render
from django.views.generic import DetailView
from .models import Trading



class TradingLineView(DetailView):
    model = Trading
    context_object_name = 'trading'
    queryset = Trading.objects.published()
    template_name = 'trading_line.html'