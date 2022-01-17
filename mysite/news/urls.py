from django.urls import path

from news.views import index, get_category, view_news, add_news, feedback

urlpatterns = [
    path('', index, name="home"),
    path('category/<int:category_id>/', get_category, name="category"),
    path('news/<int:news_id>/', view_news, name="view_news"),
    path('news/add-news/', add_news, name='add_news'),
    path('news/feedback/', feedback, name='feedback'),

]
