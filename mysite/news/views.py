from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, World!")


def test(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Тестовая страница.")
