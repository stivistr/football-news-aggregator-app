from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic as views

UserModel = get_user_model()


class ListArticleView(views.ListView):
    template_name = 'news/list_articles.html'
    model = UserModel
