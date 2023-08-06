from django.urls import path
from football_news_aggregator.news.views import CreateArticleView

urlpatterns = [
    path('articles/', CreateArticleView.as_view(), name='create_article'),
]