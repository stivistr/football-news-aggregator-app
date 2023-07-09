from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login
from django.contrib.auth.mixins import LoginRequiredMixin
from football_news_aggregator.accounts.forms import CreateUserForm, CreateProfileForm
from football_news_aggregator.accounts.models import Profile


def index(request):
    return render(request, template_name='common/base.html')


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register_page.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        profile = Profile(user=self.object)
        profile.save()

        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'


class LogoutUserView(auth_views.LogoutView):
    pass


class UpdateProfileView(LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/edit_profile.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)
