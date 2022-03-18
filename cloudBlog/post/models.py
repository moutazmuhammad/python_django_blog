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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default=' ')
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering= ('-created',)

    def __str__(self):
        return self.title


