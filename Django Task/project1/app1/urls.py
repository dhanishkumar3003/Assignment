from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_page),
    path("aboutus",views.aboutus),
    path("posts",views.post),
    path("form", views.CreateProfileView.as_view(), name='post_create'),
    path("addauthorform", views.CreateAuthorView.as_view(), name='author_create'),
    path("addcommentform", views.CreateCommentView.as_view(), name='comment_create'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('success', views.success),
]