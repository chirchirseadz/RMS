from django.shortcuts import redirect, render
from . models import CustomUser, UserProfile
from . forms import UserRegisterForm, UserProfileForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import User

# Create your views here.

@transaction.atomic
def register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            data = register_form.save(commit=False)
            data.is_tenant = True
            data.save()
            return  redirect('login')
    else:
        register_form = UserRegisterForm()
    context = {
         'register_form': register_form
    }

    return render(request, 'users/register.html', context)

@login_required(login_url='login')
def profile(request):
    return render(request, 'users/profile.html')


def ProfileUpdate(request):    
    profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
    user_form = UserUpdateForm(request.POST, instance=request.user)
    if request.method == 'POST':
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Profile Updated Successfully !!')
            return redirect('index_page')
    else:
        profile_form = UserProfileForm(instance=request.user.userprofile)
        user_form = UserUpdateForm(instance=request.user)
    context = {
       
        'profile_form': profile_form,
        'user_form': user_form,
    }
    return render(request, 'users/update_profile.html', context)



