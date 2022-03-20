from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import CreateUserFrom
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from post.models import Category

# Create your views here.
def signupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserFrom()
        categories = Category.objects.all()
        if request.method == "POST":
            form = CreateUserFrom(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Created Successfully")
                return redirect('signin')
        context = {'form': form,
                'categories': categories
        }
        return render(request, 'signup.html', context)

def allUsers(request):
    st = User.objects.all()
    context = {"all_users": st}
    return render(request, 'manage-users.html', context)



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
