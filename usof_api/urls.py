from django.urls import path, include
from .views import PostApiView
from .auth_views import register, loginView
from .user_views import UsersView

urlpatterns = [
    path('post/', PostApiView.as_view()),
    path('auth/register/', register),
    path('users/<str:username>/', UsersView.as_view()),
    path('users/', UsersView.as_view(), name='users'),
    path('auth/login/', loginView)
]
