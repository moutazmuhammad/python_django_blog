from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.allPosts, name="allposts"),
    path('post/<postID>', views.showPost, name="post"),
    path('editpost/<postID>', views.postEdit, name="editpost"),
    path('deletepost/<postID>', views.postDelete, name="deletepost"),
    path('like/', views.likePost, name='like-post'),
    path('dislike/', views.dislikePost, name='dislike-post'),
    path('add_cat/', views.add_cat, name="add_cat"),
    path('add_tag/', views.add_tag, name="add_tag"),
]
