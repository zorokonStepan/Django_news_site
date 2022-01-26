from django.urls import path

from news.views import HomeNews, NewsByCategory, ViewNews, CreateNews, CreateFeedback, test, register, login

# index, get_category, view_news, add_news, feedback,

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('test/', test, name='test'),
    # path('', index, name="home"),
    path('', HomeNews.as_view(), name="home"),
    # path('category/<int:category_id>/', get_category, name="category"),
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title': 'Категория'}), name="category"),
    # path('news/<int:news_id>/', view_news, name="view_news"),
    path('news/<int:pk>/', ViewNews.as_view(), name="view_news"),
    # path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    # path('news/feedback/', feedback, name='feedback'),
    path('news/feedback/', CreateFeedback.as_view(), name='feedback')
]
