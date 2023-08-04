from django.urls import path
from football_news_aggregator.news.views import ListArticleView

urlpatterns = [
    path('articles/', ListArticleView.as_view(), name='list_articles'),
]