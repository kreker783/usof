from django.urls import path

import usof_api.comments.views as views


urlpatterns = [
    # path('<str:category>/posts/', views.PostsCategoriesView.as_view()),
    path('<int:comment_id>/', views.SpecificCommentView.as_view()),
    path('', views.CommentView.as_view()),
]