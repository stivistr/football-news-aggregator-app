from django.urls import path

from football_news_aggregator.accounts.views import index

urlpatterns = [
    path('', index, name='index')
]