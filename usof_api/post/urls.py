from django.urls import path, include

import usof_api.post.views as views


urlpatterns = [
    path('<int:post_id>/comments/', include('usof_api.comments.urls')),
    path('<int:post_id>/categories/', views.CategoriesPostView.as_view()),
    path('<int:post_id>/', views.SpecificPostView.as_view()),
    path('', views.PostApiView.as_view()),
]
