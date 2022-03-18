from contextlib import redirect_stderr
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.contrib.auth import login , authenticate, logout
from django.contrib import messages
from post.models import Post, Comment
from post.form import PostForm
from  django.contrib.auth.models import User

def home(request):
    return redirect('main')

def signin(request):
    
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == 'POST':
                enteredUsername = request.POST.get("username")
                enteredPassword = request.POST.get("password")
                user = authenticate(username=enteredUsername , password= enteredPassword)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        if request.GET.get('next') is not None:  
                            return redirect(request.GET.get('next'))
                        else:
                            return redirect("main")
                    else:
                        messages.info(request,"You're Blocked by the admin")
                else:
                    messages.info(request,"Invalid username or password")
                    return redirect("signin")
        return render(request, "signin.html")

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('main')
    else:
        return redirect('main')
        