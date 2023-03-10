from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'profile_picture']
