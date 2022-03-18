from contextlib import redirect_stderr
from email import message
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
                if user is None:
                    try:
                        loguser = User.objects.get(username=enteredUsername)
                        if loguser.is_active and loguser is not None :
                            messages.info(request,"Invalid username or password")
                            return redirect("signin")
                        else:
                            messages.info(request,"sorry you are blocked contact the admin")
                    except:
                        messages.info(request,"Invalid username or password")                        
                else:
                    login(request,user)
                    if request.GET.get('next') is not None:  
                            return redirect(request.GET.get('next'))
                    else:
                        return redirect("main")
        return render(request, "signin.html")

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('main')
    else:
        return redirect('main')
        