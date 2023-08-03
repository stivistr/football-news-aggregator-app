from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from football_news_aggregator.accounts.forms import CreateUserForm, UpdateProfileForm, DeleteProfileForm
from football_news_aggregator.accounts.models import Profile

UserModel = get_user_model()


def index(request):
    return render(request, template_name='common/home_page.html')


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
    form_class = UpdateProfileForm
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


class ProfileDetailsView(views.DetailView):
    template_name = 'accounts/details_profile.html'
    model = Profile

    def get_context_data(self, **kwargs):
        profile_picture = static('images/image_person.jpg')
        profile = self.get_object()

        if profile.profile_picture is not None:
            profile_picture = profile.profile_picture

        context = super().get_context_data(**kwargs)
        context['profile_picture'] = profile_picture

        return context


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/delete_profile.html'
    model = Profile

    def get_success_url(self):
        return reverse_lazy('index')