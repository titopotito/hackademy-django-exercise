from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import EditUserForm, EditProfileForm, RegisterForm
import os


def home_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            return redirect('login')


@login_required(login_url='login')
def profile_view(request):
    if request.method == 'GET':
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


def register_view(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'GET':
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'register.html', context)

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save()
            user = User.objects.get(pk=new_user.id)
            new_profile = Profile(user=user)
            new_profile.save()
            return redirect('login')
        else:
            return redirect('register')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'GET':
        login_form = AuthenticationForm()
        context = {'login_form': login_form}
        return render(request, 'login.html', context)

    if request.method == 'POST':
        login_form = AuthenticationForm(None, request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('profile')
        else:
            return redirect('login')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
