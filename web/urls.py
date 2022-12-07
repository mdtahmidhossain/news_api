from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('home', views.home),
    path('news_listing', views.NewsListView.as_view(), name='news'),
    path('json_listing', views.json_endpoint, name='news_json')
]
