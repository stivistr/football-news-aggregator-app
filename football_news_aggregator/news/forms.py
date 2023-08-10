from django import forms
from football_news_aggregator.news.models import NewsArticle


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = '__all__'
