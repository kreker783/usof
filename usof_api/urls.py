from django.urls import path, include

urlpatterns = [
    path('post/', include('usof_api.post.urls')),
    path('auth/', include('usof_api.auth.urls')),
    path('users/', include('usof_api.user.urls')),
    path('categories/', include('usof_api.categories.urls')),
    path('comments/', include('usof_api.comments.urls')),
]
