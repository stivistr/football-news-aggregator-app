from django.urls import path
from football_news_aggregator.news.views import CreateArticleView, article_list

urlpatterns = [
    path('articles/', CreateArticleView.as_view(), name='create_article'),
    path('all_articles/', article_list, name='list_articles'),
]