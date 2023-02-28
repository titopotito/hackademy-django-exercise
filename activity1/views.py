from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import EditUserForm, EditProfileForm
import os


def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')


@login_required(login_url='login')
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def edit_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    old_image_path = profile.profile_picture.path

    if request.method == 'GET':
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'edit_profile.html', context)

    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid():
            if profile_form.is_valid():
                if request.FILES.get('profile_picture'):
                    os.remove(old_image_path)
                user_form.save()
                profile_form.save()
                return redirect('profile')
        return redirect('edit_profile')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

    return render(request, 'login.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
