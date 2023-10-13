from django.urls import path, include
from .views import PostApiView
from .auth_views import register
from .user_views import get_users

urlpatterns = [
    path('post/', PostApiView.as_view()),
    path('auth/register/', register),
    path('users/', get_users),
]
