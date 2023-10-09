from django.urls import path, include
from .views import PostApiView

urlpatterns = [
    path('post/', PostApiView.as_view())
]
