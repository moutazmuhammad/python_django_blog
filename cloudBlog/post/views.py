from turtle import pos
from django.shortcuts import render, redirect, HttpResponse
from .models import Post
from .form import CommentForm, PostForm, EditPostForm


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
    # To enter a new comment
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False) # commit=False means not save yet
            instance.user = request.user # send user name with comment
            instance.post = post # make relation between post and comment
            instance.save()
            return redirect('post', postID = post.id)
    else:
        comment_form = CommentForm()
    context = {
        'post': post,   
        'comment_form': comment_form
        }
    return render(request, 'post.html', context)


def postEdit(request, postID):
    if request.user.is_authenticated:
        post = Post.objects.get(id = postID)
        form = EditPostForm(instance=post)
        if request.method=='POST':
            form = EditPostForm(request.POST, request.FILES, instance=post)
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
    else:
        return redirect('allposts')


def postDelete(request, postID):
    if request.user.is_authenticated and request.user.is_superuser:
        post = Post.objects.get(id=postID)
        post.delete()
    return redirect('allposts')

