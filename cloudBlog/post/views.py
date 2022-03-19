#from tkinter import Y
#from turtle import pos
from django.shortcuts import render, redirect, HttpResponse
from .models import Post, Like, Dislike, Category, Tags
from .form import CommentForm, PostForm, EditPostForm, CategoryForm, TagsForm
from post.models import Post, Comment, Category, Tags

def add_cat(request):
    if request.user.is_authenticated and request.user.is_superuser:
        form = CategoryForm()
        if request.method == "POST":
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('allposts')
        context = {'form': form}
        return render(request, 'add_cat.html', context)
    else:
        return redirect('allposts')   

def add_tag(request):
    if request.user.is_authenticated and request.user.is_superuser:
        form = TagsForm()
        if request.method == "POST":
            form = TagsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('allposts')
        context = {'form': form}
        return render(request, 'add_tag.html', context)
    else:
        return redirect('allposts') 

# Create your views here.

def allPosts(request):
    posts = Post.objects.order_by('-created')[:5] 
    form = PostForm()
    categories = Category.objects.all()
    tags = Tags.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save_m2m()
            return redirect('allposts')
        else:
            form = PostForm()
    context = {
        'allposts': posts,
        'form': form,
        'categories': categories,
        'tags' :tags,
        }
    return render(request, 'allposts.html', context)

def categoryPosts(request, categoryID):
    posts = Post.objects.filter(category= categoryID)
    form = PostForm()
    categories = Category.objects.all()
    tags = Tags.objects.all()
    context = {
        'allposts': posts,
        'form': form,
        'categories': categories,
        'tags': tags,
        }
    return render(request, 'allposts.html', context)

def tagPosts(request, tagID):
    posts = Post.objects.filter(tags= tagID)
    form = PostForm()
    tags = Tags.objects.all()
    categories = Category.objects.all()
    context = {
        'allposts': posts,
        'form': form,
        'categories': categories,
        'tags': tags,
        }
    return render(request, 'allposts.html', context)

def showPost(request, postID):
    post = Post.objects.get(id = postID)
    categories = Category.objects.all()
    tags = Tags.objects.all()
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
        'comment_form': comment_form,
        'categories': categories,
        'tags': tags,
        }
    return render(request, 'post.html', context)


def postEdit(request, postID):
    if request.user.is_authenticated:
        post = Post.objects.get(id = postID)
        form = EditPostForm(instance=post)
        categories = Category.objects.all()
        tags = Tags.objects.all()
        if request.method=='POST':
            form = EditPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post', postID=post.id)
            else:
                form = EditPostForm(instance=post)

        context = {
            'post': post, 
            'form': form,
            'categories': categories,
            'tags': tags,
            }
        return render(request, 'editpost.html', context)
    else:
        return redirect('allposts')


def postDelete(request, postID):
    if request.user.is_authenticated and request.user.is_superuser:
        post = Post.objects.get(id=postID)
        post.delete()
    return redirect('allposts')

def likePost(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            post_id = request.POST.get('post_id')
            post_obj = Post.objects.get(id=post_id)

            if user in post_obj.liked.all():
                post_obj.liked.remove(user)
                post_obj.disliked.add(user)
            else:
                post_obj.liked.add(user)
                post_obj.disliked.remove(user)
            
            post_obj.save()
    return redirect('allposts')

def dislikePost(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            post_id = request.POST.get('post_id')
            post_obj = Post.objects.get(id=post_id)

            if user in post_obj.disliked.all():
                post_obj.disliked.remove(user)
                post_obj.liked.add(user)
            else:
                post_obj.disliked.add(user)
                post_obj.liked.remove(user)
            
            post_obj.save()
    return redirect('allposts')
