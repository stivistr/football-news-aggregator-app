from django.urls import path, include
from football_news_aggregator.accounts.views import index, RegisterUserView, LoginUserView, LogoutUserView, \
    UpdateProfileView, ProfileDetailsView, delete_profile

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='details_profile'),
        path('edit/', UpdateProfileView.as_view(), name='edit_profile'),
        path('delete/', delete_profile, name='delete_profile'),
    ]))
]