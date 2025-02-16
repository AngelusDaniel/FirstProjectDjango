from typing import Any

from blog.data import posts
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def blog(request):
    print("Milion")

    context = {
        #"text": "Estamos no blog",
        "title": "Blog",
        "posts": posts
    }

    return render(
        request,
        "blog/index.html",
        context
        )


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post["id"] == post_id:
            found_post = post

    if found_post is None:
        raise Http404("Post não existe")


    context = {
        #"text": "Estamos no blog",
        "title": found_post["title"],
        "post": found_post
    }

    return render(
        request,
        "blog/post.html",
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
