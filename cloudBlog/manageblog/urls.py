
from django.contrib import admin
from django.urls import path, include
from . import  views


urlpatterns = [
  #Manges Users Urls
  path('all-users/', views.allUsers, name='all-users'),
  path('show-user/<userid>', views.showUser, name='show-user'),
  path('del-user/<userid>', views.delUser, name='del-user'),
  path('block-user/<userid>', views.blockUser, name='block-user'),
  path('unblock-user/<userid>', views.unblockUser, name='unblock-user'),
#Manges Posts Urls
  path('all-posts/', views.allPosts, name='all-posts'),
  path('add-post/', views.addPost, name='add-post'),


]
