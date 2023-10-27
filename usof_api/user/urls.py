from django.urls import path
import usof_api.user.views as views

urlpatterns = [
    path('avatar/', views.avatar_user),
    path('current_user/', views.get_current_user),
    path('<str:username>/', views.SpecificUserView.as_view()),
    path('', views.UsersView.as_view(), name='users'),
]
