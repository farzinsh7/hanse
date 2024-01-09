from django.urls import path
from .views import TradingLineView


app_name = "trading"
urlpatterns = [
    path('<slug:slug>', TradingLineView.as_view(), name='line'),
]