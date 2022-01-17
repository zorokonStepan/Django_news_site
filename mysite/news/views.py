from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category, Feedback
from .forms import NewsForm, FeedbackForm


def index(request: HttpRequest) -> HttpResponse:
    news = News.objects.all()
    context = {"news": news, "title": "Список новостей"}
    return render(request=request, template_name='news/index.html', context=context)


def get_category(request: HttpRequest, category_id: int) -> HttpResponse:
    news = News.objects.filter(category_id=category_id)
    # category = Category.objects.get(pk=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {"news": news, "category": category}
    return render(request=request, template_name='news/category.html', context=context)


def view_news(request: HttpRequest, news_id: int) -> HttpResponse:
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    context = {"news_item": news_item}
    return render(request=request, template_name='news/view_news.html', context=context)


# связ с формами
def add_news(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # News.objects.create(**form.cleaned_data)
            news = form.save()
            # return redirect(news)
            return redirect('add_news')
    else:
        form = NewsForm()
    return render(request=request, template_name='news/add_news.html', context={'form': form})


# # не связ с формами
# def add_news(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             News.objects.create(**form.cleaned_data)
#             # return redirect('home')
#             return redirect('add_news')
#     else:
#         form = NewsForm()
#     return render(request=request, template_name='news/add_news.html', context={'form': form})

# не связ с формами
def feedback(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedback.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request=request, template_name='news/feedback.html', context={'form': form})

# def feedback(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = FeedbackForm()
#     return render(request=request, template_name='news/feedback.html', context={'form': form})
