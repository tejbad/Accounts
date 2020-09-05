from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
# from .forms import UserForm
from django import forms
from django.conf import settings
import urllib
import json

@login_required(login_url="/accounts/login")
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        clg_name = request.POST.get('clg_name')
        degree = request.POST.get('degree')
        course = request.POST.get('course')
        passout_year = request.POST.get('passout_yr')
        school_name = request.POST.get('school_name')
        age = request.POST.get('age')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username ,first_name=first_name, password=password1, email=email, last_name=last_name,clg_name= clg_name, age=age,school_name=school_name,passout_year=passout_year,course=course,degree=degree)
                user.save()
                return redirect('login')
        else:
            messages.error(request,'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required(login_url="/accounts/login")
def logout(request):
    auth.logout(request)
    return redirect('/')

