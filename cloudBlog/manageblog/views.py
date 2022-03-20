from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from post.models import Post

from django.contrib import messages
# Create your views here.
def allUsers(request):
    if request.user.is_authenticated:
        st = User.objects.all()
        context = {"all_users": st}
        return render(request, 'manage-users.html', context)
    return redirect('main')


def showUser(request, userid):
    userID = User.objects.get(id=userid)
    context = {'id': userID}
    return render(request, 'show-user.html', context)


def delUser(request, userid):
    user = User.objects.get(id=userid)
    user.delete()
    return redirect('all-users')

def blockUser(request,userid):
    user = User.objects.get(id=userid)
    user.is_active = False
    user.save()
    return redirect('all-users')

def unblockUser(request,userid):
    user = User.objects.get(id=userid)
    user.is_active = True
    user.save()
    return redirect('all-users')

#Posts

def allPosts(request):
    if request.user.is_authenticated:
        post = Post.objects.all()
        context = {"all_posts": post}
        return render(request, 'manage-posts.html', context)
    return redirect('main')

def addPost(request):
    if request.user.is_authenticated:
       return redirect('main')
# def editUser(request, userid):
#     if request.user.is_authenticated:
#         user = User.objects.get(id=userid)
#         userform = UserCreationForm(instance=user)
#         if request.method == 'POST':
#             userform = UserCreationForm(request.POST, instance=user)
#             if userform.is_valid():
#                 userform.save()
#                 return redirect('all-users')
#         context = {'form': userform, 'id':userid}
#         return render(request, 'show-user.html', context)
#     return redirect('main')