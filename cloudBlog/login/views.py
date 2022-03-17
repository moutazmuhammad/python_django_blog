from contextlib import redirect_stderr
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.contrib.auth import login , authenticate, logout
from django.contrib import messages

from  django.contrib.auth.models import User

def home(request):
    return render(request, 'base.html')

def signin(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
                enteredUsername = request.POST.get("username")
                enteredPassword = request.POST.get("password")
                user = authenticate(username=enteredUsername , password= enteredPassword)
                if user is not None:
                    login(request,user)
                    if request.GET.get('next') is not None:  
                        return redirect(request.GET.get('next'))
                    else:
                        return redirect("home")
                else:
                    messages.info(request,"Invalid username or password")
        return render(request, "signin.html")

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('home')
        