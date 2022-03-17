from unicodedata import name
from django.urls import  path
from . import views
urlpatterns = [
    # path('register/', views.register , name='register'),
    path('home/' ,  views.home , name= 'home'),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name='signout')   
]