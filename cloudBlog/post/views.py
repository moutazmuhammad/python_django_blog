from django.shortcuts import render, redirect, HttpResponse
from .models import Post
from .form import PostForm


# Create your views here.

def allPosts(request):
    posts = Post.objects.all()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
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
    

def post(request, postID):
    post = Post.objects.get(id = postID)
    context = {'post': post}
    return render(request, 'post.html', context)

# def createPost(request):
#     posts = Post.objects.all()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allposts')
#     context = {
#         'posts': posts,
        
#         }
#     return render(request, 'allposts.html', context)
