from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')) # [''] without post dir name to enter site by localhost:8000 only
]
