from django.urls import path
from .views import Index, SiteHeaderView, SiteFooterView, create


app_name = "page"
urlpatterns = [
    path('', Index.as_view(), name = "index"),
    path('header/', SiteHeaderView.as_view(), name = "head"),
    path('footer/', SiteFooterView.as_view(), name = "foot"),
    path('create', create, name = "create"),
]