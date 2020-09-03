from django.shortcuts import render, redirect
from .form import *
from django.contrib.auth import authenticate, login
from .models import Profile

def signup(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            return redirect('/accounts/profile')
        
    else:
        form = SignupForm()
    
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'accounts/profile.html', context)

def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            myprofile = profile_form.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect('/accounts/profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance = profile)
    context = {'userform':user_form, 'profileform':profile_form}
    return render(request, 'accounts/profile_edit.html', context)