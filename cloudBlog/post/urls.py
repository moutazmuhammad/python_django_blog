from django.urls import path
from . import views

urlpatterns = [
    path('allposts/', views.allPosts, name="allposts"),
    path('post/<postID>', views.post, name="post"),
]
