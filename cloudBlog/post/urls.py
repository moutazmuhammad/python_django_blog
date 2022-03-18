from django.urls import path
from . import views

urlpatterns = [
    path('allposts/', views.allPosts, name="allposts"),
    path('post/<postID>', views.showPost, name="post"),
    path('editpost/<postID>', views.postEdit, name="editpost"),
]
