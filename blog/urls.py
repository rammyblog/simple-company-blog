from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('drafts/', views.DraftListView.as_view(), name='post_drafts'),
    path('post/<int:pk>/details', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<pk>/add/comment/', views.add_comment, name='add_comment'),
    path('comment/<pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<pk>/delete/', views.comment_delete, name='comment_delete'),
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),



]
