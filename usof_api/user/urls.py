from django.urls import path
from .views import UsersView

urlpatterns = [
    path('<str:username>/', UsersView.as_view()),
    path('', UsersView.as_view(), name='users')
]