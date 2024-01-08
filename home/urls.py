from django.urls import path
from .views import Index, SiteHeaderView, SiteFooterView


app_name = "page"
urlpatterns = [
    path('', Index.as_view(), name = "index"),
    path('header/', SiteHeaderView.as_view(), name = "head"),
    path('footer/', SiteFooterView.as_view(), name = "foot"),
]