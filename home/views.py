from django.shortcuts import render

def index(request):
    context = {"Hello": "Hello"}
    return render(request, "index.html", context)