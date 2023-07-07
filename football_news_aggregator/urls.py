from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('football_news_aggregator.news.urls')),
    path('', include('football_news_aggregator.accounts.urls')),
]
