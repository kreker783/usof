from django.urls import path
import usof_api.auth.views as views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         views.activate,
         name='activate'),

    path('login/', views.loginView),
    path('logout/', views.logoutView),

    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         views.set_password,
         name='new_password')
]
