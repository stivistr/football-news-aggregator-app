from django.urls import path
from football_news_aggregator.news.views import CreateArticleView, article_list, add_comment_view

urlpatterns = [
    path('articles/', CreateArticleView.as_view(), name='create_article'),
    path('', article_list, name='article_list'),
    path('add_comment/<int:article_id>/', add_comment_view, name='add_comment'),
]