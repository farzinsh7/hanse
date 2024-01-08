from django.urls import path
from .views import index, SiteHeaderView, SiteFooterView


app_name = "page"
urlpatterns = [
    path('', index, name = "index"),
    path('header/', SiteHeaderView.as_view(), name = "head"),
    path('footer/', SiteFooterView.as_view(), name = "foot"),
]