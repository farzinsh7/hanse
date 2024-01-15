from django.urls import path
from .views import ContactUsView, add_form


app_name = "contact"
urlpatterns = [
    path('contact-us/', ContactUsView.as_view(), name = "page"),
    path("add-form/", add_form, name="add-form")
]