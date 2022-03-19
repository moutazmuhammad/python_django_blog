from curses import meta
from distutils.command.upload import upload
from operator import mod
from pyexpat import model
from turtle import pos
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
    liked = models.ManyToManyField(User, blank=True, default=None, related_name= 'liked')
    disliked = models.ManyToManyField(User, blank=True, default=None, related_name= 'disliked')

    class Meta:
        ordering= ('-created',)

    # To get number of comment use relationship between Post and Comment models
    def comment_count(self):
        return self.comment_set.all().count()

    # To all comment use relationship between Post and Comment models
    def comments(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    comment_data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body

# LIKE_CHOICSE={
#     ('Like', 'Like'),
#     ('Dislike', 'Dislike'),
# }

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.value

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.value