from django.urls import path, include

import usof_api.comments.views as views
import usof_api.like.views as LikeViews


urlpatterns = [
    # path('<str:category>/posts/', views.PostsCategoriesView.as_view()),
    path('<int:id>/like/', LikeViews.CommentLikeView.as_view()),
    path('<int:comment_id>/', views.SpecificCommentView.as_view()),
    path('', views.CommentView.as_view()),
]