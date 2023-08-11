from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from football_news_aggregator.news.forms import CreateArticleForm, AddCommentForm
from football_news_aggregator.news.models import NewsArticle


class CreateArticleView(views.CreateView):
    template_name = 'news/create_article.html'
    form_class = CreateArticleForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def article_list(request):
    articles = NewsArticle.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'common/home_page.html', context)


def add_comment_view(request, article_id):
    article = NewsArticle.objects.get(pk=article_id)

    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            new_comment_instance = form.save(commit=False)
            new_comment_instance.to_article = article
            new_comment_instance.save()

            return redirect('index')

    context = {
        'article': article,
        'form': AddCommentForm(),
    }

    return render(request, template_name='common/add_comment.html', context=context)
