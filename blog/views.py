from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def blog(request):
    print("Milion")

    context = {
        "text": "Estamos no blog",
        "title": "Blog",
    }

    return render(
        request,
        "blog/index.html",
        context
        )


def exemplo(request):
    print("Posso fazer qualquer coisa")
    context = {
        "text": "Estamos no blog/exemplo",
        "title": "Blog",
    }
    return render(
        request,
        "blog/exemplo.html",
        context
        )
