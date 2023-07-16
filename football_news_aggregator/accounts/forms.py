from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from football_news_aggregator.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from football_news_aggregator.accounts.models import Profile

UserModel = get_user_model()


class CreateUserForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


class ProfileDetailForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


class DeleteProfileForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

