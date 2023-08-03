from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from football_news_aggregator.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from football_news_aggregator.news.models import NewsArticle


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = '__all__'