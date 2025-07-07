from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileForm
from django.db import transaction

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'basic_app/index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
               login(request,user)
               return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("someone tried to login and failed")
            print('username:{} and password {}'.format(username,password))
            return HttpResponse("Invalid login details")
    else:
        return render(request,'basic_app/login.html')
    

@ login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def special(request):
    return HttpResponse("You are logged in")


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data['password1']) 
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                messages.error(request, "Invalid login details.")
                return render(request, 'basic_app/login.html')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()

    return render(request, 'basic_app/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
