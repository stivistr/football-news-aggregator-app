from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from football_news_aggregator.news.forms import CreateArticleForm
UserModel = get_user_model()


class CreateArticleView(views.CreateView):
    template_name = 'news/create_article.html'
    form_class = CreateArticleForm
    success_url = reverse_lazy('index')


