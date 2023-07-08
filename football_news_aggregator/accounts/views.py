from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth import views as auth_views


# Create your views here.

def index(request):
    return render(request, template_name='common/base.html')


class RegisterUserView(views.CreateView):
    pass


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'


class LogoutUserView(auth_views.LogoutView):
    pass
