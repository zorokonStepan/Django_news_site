from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import News


def index(request: HttpRequest) -> HttpResponse:
    # news = News.objects.order_by('-created_at')
    news = News.objects.all()
    return render(request=request,
                  template_name='news/index.html',
                  context={"news": news, "title": "Список новостей"})
