from django.urls import path, include
from .views import PostApiView
from .auth_views import register, loginView, logoutView
from .user_views import UsersView

urlpatterns = [
    path('post/', PostApiView.as_view()),
    path('auth/register/', register),
    path('users/', include('usof_api.user.urls')),
    path('auth/login/', loginView),
    path('auth/logout', logoutView)
]
