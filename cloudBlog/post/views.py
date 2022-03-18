from turtle import pos
from django.shortcuts import render, redirect, HttpResponse
from .models import Post
from .form import PostForm, EditPostForm


# Create your views here.

def allPosts(request):
    posts = Post.objects.all()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('allposts')
        else:
            form = PostForm()
    context = {
        'allposts': posts,
        'form': form,
        }
    return render(request, 'allposts.html', context)
    

def showPost(request, postID):
    post = Post.objects.get(id = postID)
    context = {'post': post}
    return render(request, 'post.html', context)


def postEdit(request, postID):
    post = Post.objects.get(id = postID)
    form = EditPostForm(instance=post)
    if request.method=='POST':
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post', postID=post.id)
        else:
            form = EditPostForm(instance=post)

    context = {
        'post': post, 
        'form': form
        }
    return render(request, 'editpost.html', context)

def postDelete(request, postID):
    post = Post.objects.get(id=postID)
    post.delete()
    return redirect('allposts')


