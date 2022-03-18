from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from post.views import allPosts

urlpatterns = [
    path('', allPosts, name='main'),
    path('admin/', admin.site.urls, name='admin'),
    path('', include('post.urls')), # [''] without post dir name to enter site by localhost:8000 only
    path('', include('signup.urls')),
    path('', include('login.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
