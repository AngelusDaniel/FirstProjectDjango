
from django.shortcuts import render

# Create your views here.

def home(request):
    print("Home")
    context = {
        "text": "Estamos na home"
    }
    return render(
        request,
        "home/index.html",
        context
        )