from django.urls import path, include
from .views import PostApiView
from

urlpatterns = [
    path('post/', PostApiView.as_view())
]
