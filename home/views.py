from django.shortcuts import render
from .models import SiteInformation
from django.views.generic import ListView

def index(request):
    context = {"Hello": "Hello"}
    return render(request, "index.html", context)



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