from django.shortcuts import render
from .models import SiteInformation, HomeData
from django.views.generic import ListView
from trading_line.models import Trading
from investment_line.models import Investment

class Index(ListView):
    model = HomeData
    template_name = 'index.html'
    context_object_name = "home"
    queryset = HomeData.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trading'] = Trading.objects.published()[:3]
        context['investment'] = Investment.objects.published()[:3]
        return context



class SiteHeaderView(ListView):
    model = SiteInformation
    template_name = 'base/shared/header.html'
    context_object_name = 'info'
    queryset = SiteInformation.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trading'] = Trading.objects.published()[:5]
        context['investment'] = Investment.objects.published()[:5]
        return context


class SiteFooterView(ListView):
    model = SiteInformation
    template_name = 'base/shared/footer.html'
    context_object_name = 'info'
    queryset = SiteInformation.objects.first()