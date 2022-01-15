from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import News, Category


def index(request: HttpRequest) -> HttpResponse:
    news = News.objects.all()
    context = {"news": news, "title": "Список новостей"}
    return render(request=request, template_name='news/index.html', context=context)


def get_category(request: HttpRequest, category_id: int) -> HttpResponse:
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {"news": news, "category": category}
    return render(request=request, template_name='news/category.html', context=context)



