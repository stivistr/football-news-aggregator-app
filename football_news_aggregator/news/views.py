from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from football_news_aggregator.news.forms import CreateArticleForm
from football_news_aggregator.news.models import NewsArticle


class CreateArticleView(views.CreateView):
    template_name = 'news/create_article.html'
    form_class = CreateArticleForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if form.is_valid():
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


def article_list(request):
    articles = NewsArticle.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'common/home_page.html', context)
