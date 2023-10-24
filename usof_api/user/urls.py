from django.urls import path
from .views import UsersView, get_current_user

urlpatterns = [
    path('<str:username>/', UsersView.as_view()),
    path('', UsersView.as_view(), name='users'),
    path('avatar/', UsersView.as_view()),
    path('current_user/', get_current_user)
]
