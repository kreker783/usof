from django.urls import path

import usof_api.categories.views as views


urlpatterns = [
    path('<str:category>/posts/', views.PostsCategoriesView.as_view()),
    path('<str:category>/', views.SpecificCategoryView.as_view()),
    path('', views.CategoryApiView.as_view()),
]
