from django.shortcuts import render
from django.views import generic as views

# Create your views here.

def index(request):
    return render(request, template_name='common/base.html')


class RegisterUserView(views.CreateView):
    pass
