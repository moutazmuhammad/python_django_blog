from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from post.models import Post,Category
from post.form import CategoryForm


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
def adminUser(request,userid):
    user = User.objects.get(id=userid)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    return redirect('all-users')

def unadminUser(request,userid):
    user = User.objects.get(id=userid)
    user.is_superuser = False
    user.is_staff = False
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


#Categories
def allCats(request):
    if request.user.is_authenticated:
        cat = Category.objects.all()
        context = {"all_cats": cat}
        return render(request, 'manage-cat.html', context)
    return redirect('main')

def delCat(request, catid):
    if request.user.is_authenticated:
        cat = Category.objects.get(id=catid)
        cat.delete()
        return redirect('all-cats')
    return redirect('main')

def addCat(request):
    if request.user.is_authenticated and request.user.is_superuser:
        form = CategoryForm()
        if request.method == "POST":
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('all-cats')
        context = {'form': form}
        return render(request, 'addCat.html', context)
    else:
        return redirect('all-cats')

# def editCat(request, catid):
#     if request.user.is_authenticated:
#         cat = Category.objects.get(id = catid)
#         form = CategoryForm(instance=cat)  
#         if request.method=='POST':
#             form = CategoryForm(request.POST, instance=cat)
#             if form.is_valid():
#                 form.save()
#                 return redirect('all-cats')
#             else:
#                 form = CategoryForm(instance=cat)
# 
#         context = {
#          
#             'categories': categories,
#           
#             }
#         return render(request, 'edit-cat.html', context)
#     else:
#         return redirect('all-cats')


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