from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed

app_name = 'blog'


urlpatterns = [
    path('', blog_index_view, name='index'),
    path('single/<int:pid>', blog_single_view, name='single'),
    path('category/<str:cat>', blog_index_view, name='category'),
    path('tag/<str:tag>', blog_index_view, name='tag'),
    path('author/<str:author>', blog_index_view, name='author'),
    path('search/', blog_search_view, name='search'),
    path('rss/feed/', LatestEntriesFeed()),
]