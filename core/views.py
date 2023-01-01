from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import CreatorPost, videoObject
from .forms import videoObjectCreationForm

# Create your views here.

# posts = [
#     {'id':1, 'name':'Post 1'},
#     {'id':2, 'name':'Post 2'},
#     {'id':3, 'name':'Post 3'}
# ]

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    posts = CreatorPost.objects.filter(
        Q(post_title__icontains=q) |
        Q(post_content__icontains=q))


    ctx = {
        'posts':posts
    }

    return render(request, 'core/home.html', ctx)


def loginPage(request):
    pagetype = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'The Username or Password provided are Invalid')

    ctx = {
        'pagetype': pagetype
    }
    return render(request, 'core/login-register.html', ctx)


def logoutUserView(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    pagetype = 'register'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # access immediately
            user.username = user.username.lower()  # ignores numbers and other things when making lower
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
            print(form)
    form = UserCreationForm

    ctx = {
        'pagetype': pagetype,
        'form': form
    }

    return render(request, 'core/login-register.html', ctx)

def creatorPostPage(request, pk):
    post = CreatorPost.objects.get(id=pk)

    ctx = {
        'post':post
    }
    return render(request, 'core/creator-post.html', ctx)


def videoViewingPage(request, pk): # temp using pk:id, switch to UUID!

    video_object = videoObject.objects.get(id=pk)
    video_raw = video_object.rawvideo

    ctx = {
        'video_raw':video_raw,
        'video_object':video_object
    }

    return render(request, 'core/video.html', ctx)
