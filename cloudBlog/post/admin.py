from django.contrib import admin
from .models import Post, Comment, Like, Dislike, Category, Tags
from django.contrib.auth.models import Group, User
# Register your models here.
# admin.site.site_header = "News Cloud Blog"
# admin.site.site_title = "News Cloud Blog"
#
#
#   # title = models.CharField(max_length=100)
#   #   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   #   body = models.TextField(default=' ')
#   #   image = models.ImageField(blank=True, null=True, upload_to='images/')
#   #   created = models.DateTimeField(default=timezone.now)
#   #   liked = models.ManyToManyField(User, blank=True, default=None, related_name= 'liked')
#   #   disliked = models.ManyToManyField(User, blank=True, default=None, related_name= 'disliked')
# 	# #category foreign
#   #   category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
# 	# #tag manytomany
#   #   tags = models.ManyToManyField(Tags)
#
# class PostAdmin(admin.ModelAdmin):
#     fields = ('title', 'user', 'body','created', 'category','tags')


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.unregister(Group)