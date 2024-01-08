from django.urls import path
from .views import ContactUsView


app_name = "contact"
urlpatterns = [
    path('contact-us/', ContactUsView.as_view(), name = "page"),
]