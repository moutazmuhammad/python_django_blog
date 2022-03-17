from curses import meta
from distutils.command.upload import upload
from operator import mod
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User.first_name)
    body = models.TextField(default=' ')
    image = models.ImageField(upload_to='postImages/', default='postImages/default.png')
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering= ('-created',)

    def __str__(self):
        return self.title


