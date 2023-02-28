from django.forms import ModelForm
from .models import Profile, User


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'profile_picture']
