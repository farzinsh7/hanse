from django.urls import path
from .views import InvestmentLineView


app_name = "investment"
urlpatterns = [
    path('<slug:slug>', InvestmentLineView.as_view(), name='line'),
]