from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from football_news_aggregator.common.helpers import BootstrapFormMixin
from football_news_aggregator.accounts.models import Profile

UserModel = get_user_model()


class CreateUserForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2')


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
