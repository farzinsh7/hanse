from django.shortcuts import render
from .models import SiteInformation, HomeData
from django.views.generic import ListView

class Index(ListView):
    model = HomeData
    template_name = 'index.html'
    context_object_name = "home"
    queryset = HomeData.objects.first()



class SiteHeaderView(ListView):
    model = SiteInformation
    template_name = 'base/shared/header.html'
    context_object_name = 'info'
    queryset = SiteInformation.objects.first()


class SiteFooterView(ListView):
    model = SiteInformation
    template_name = 'base/shared/footer.html'
    context_object_name = 'info'
    queryset = SiteInformation.objects.first()