from django.urls import path
# from django.views.decorators.cache import cache_page

from news.views import HomeNews, NewsByCategory, ViewNews, CreateNews, CreateFeedback, contact, register, \
    user_login, user_logout

# index, get_category, view_news, add_news, feedback,

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact/', contact, name='contact'),
    # path('', index, name="home"),

    path('', HomeNews.as_view(), name="home"),
    # path('', cache_page(60)(HomeNews.as_view()), name="home"),

    # path('category/<int:category_id>/', get_category, name="category"),
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title': 'Категория'}), name="category"),
    # path('news/<int:news_id>/', view_news, name="view_news"),
    path('news/<int:pk>/', ViewNews.as_view(), name="view_news"),
    # path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    # path('news/feedback/', feedback, name='feedback'),
    path('news/feedback/', CreateFeedback.as_view(), name='feedback')
]
