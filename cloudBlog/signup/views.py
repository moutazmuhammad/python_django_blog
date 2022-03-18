from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import CreateUserFrom
from django.contrib import messages
from .models import *
# Create your views here.
def signupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserFrom()
        if request.method == "POST":
            form = CreateUserFrom(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Created Successfully")
                return redirect('signin')
        context = {'form': form}
        return render(request, 'signup.html', context)
