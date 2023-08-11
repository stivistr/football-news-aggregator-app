from django import forms
from football_news_aggregator.news.models import NewsArticle, Comment


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = '__all__'


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['date_time_of_publication', 'to_article']
