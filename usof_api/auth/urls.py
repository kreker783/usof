from django.urls import path
import usof_api.auth.views as views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.loginView),
    path('logout/', views.logoutView)
]