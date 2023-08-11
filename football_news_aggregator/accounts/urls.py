from django.urls import path, include
from football_news_aggregator.accounts.views import index, RegisterUserView, LoginUserView, LogoutUserView, \
    UpdateProfileView, ProfileDetailsView, ProfileDeleteView, BookmarkArticleView, FavoritesListView

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='details_profile'),
        path('edit/', UpdateProfileView.as_view(), name='edit_profile'),
        path('delete/', ProfileDeleteView.as_view(), name='delete_profile'),
    ])),
    path('favourites/', FavoritesListView.as_view(), name='bookmarks'),
    path('favourites/<int:article_id>/', BookmarkArticleView.as_view(), name='bookmark_article'),
]