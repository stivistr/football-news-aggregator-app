from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

from football_news_aggregator.accounts.forms import CreateUserForm, CreateProfileForm


def index(request):
    return render(request, template_name='common/base.html')


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register_page.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'


class LogoutUserView(auth_views.LogoutView):
    pass


class CreateProfileView(views.CreateView):
    template_name = 'accounts/create_profile.html'
    form_class = CreateProfileForm

    def form_valid(self, form):
        result = super().form_valid(form)

        return result
