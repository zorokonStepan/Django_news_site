# from django.db.models import F
# from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core import paginator
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import NewsForm, FeedbackWithForm, UserRegisterForm, UserLoginForm
from .models import News, Category

from .utils import MyMixin

from django.core.paginator import Paginator
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = messages.success(request, "Вы успешно зарегистрированны")
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserRegisterForm()
    return render(request=request, template_name='news/register.html', context={"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', context={"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


def test(request):
    objects = ['john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_objects})


class HomeNews(ListView, MyMixin):
    # class HomeNews(ListView) аналог def index(request: HttpRequest) -> HttpResponse:

    # откуда получить данные
    model = News  # аналог news = News.objects.all()

    # если хотим переопределить класс, то:
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    mixin_prop = 'hello world'
    paginate_by = 2

    # extra_context - для статических данных
    # extra_context = {'title': 'Главная'}

    # def get_context_data - для динамических данных
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    # фильтруем вывод данных
    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


# def index(request: HttpRequest) -> HttpResponse:
#     news = News.objects.all()
#     context = {"news": news, "title": "Список новостей"}
#     return render(request=request, template_name='news/index.html', context=context)

class NewsByCategory(ListView, MyMixin):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 2

    # allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context


# def get_category(request: HttpRequest, category_id: int) -> HttpResponse:
#     news = News.objects.filter(category_id=category_id)
#     # category = Category.objects.get(pk=category_id)
#     category = get_object_or_404(Category, pk=category_id)
#     context = {"news": news, "category": category}
#     return render(request=request, template_name='news/category.html', context=context)

class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'
    context_object_name = 'news_item'


# def view_news(request: HttpRequest, news_id: int) -> HttpResponse:
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {"news_item": news_item}
#     return render(request=request, template_name='news/view_news.html', context=context)


# связ с формами

class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')

    login_url = '/admin/'
    # raise_exception = True


# def add_news(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('add_news')
#     else:
#         form = NewsForm()
#     return render(request=request, template_name='news/add_news.html', context={'form': form})


# не связ с формами
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


class CreateFeedback(CreateView):
    form_class = FeedbackWithForm
    template_name = 'news/feedback.html'

# def feedback(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             Feedback.objects.create(**form.cleaned_data)
#             return redirect('home')
#     else:
#         form = FeedbackForm()
#     return render(request=request, template_name='news/feedback.html', context={'form': form})
