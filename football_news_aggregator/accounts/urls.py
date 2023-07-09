from django.urls import path
from football_news_aggregator.accounts.views import index, RegisterUserView, LoginUserView, LogoutUserView, \
    UpdateProfileView

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('profile/', UpdateProfileView.as_view(), name='edit_profile'),
]