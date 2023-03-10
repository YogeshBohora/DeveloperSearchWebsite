from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")    
        user = authenticate(request, username=username, password=password)    
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or Password is invalid")   
    return render(request, "users/login_register.html")

def logoutUser(request):
    logout(request)
    messages.error(request, "User was logged out")
    return redirect('login')

def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, "users/profiles.html", context)


def userProfile(request, pk):
    user_profile = Profile.objects.get(id=pk)
    return render(request, "users/user-profile.html", {'profile': user_profile})    