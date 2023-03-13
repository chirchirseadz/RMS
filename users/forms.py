from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import CustomUser, UserProfile


class UserRegisterForm(UserCreationForm):

    class Meta:
        model=CustomUser
        fields= ['username', 'first_name', 'last_name', 'email','password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields= ['username', 'first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone','address','profile_pic']
