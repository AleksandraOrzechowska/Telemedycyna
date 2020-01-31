from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    return render(request, "home.html",{})

def about(request):
    from app_pages.info import data
    return render(request, "about.html",{"something": data})

def login_patient(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Login error, please try again.'))
            return redirect('login_patient')
    else:
        return render(request, "login_patient.html",{})

def login_doctor(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Login error, please try again.'))
            return redirect('login_doctor')
    else:
        return render(request, "login_doctor.html",{})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('home')

def register_user(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You have registered.'))
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form' : form}
    return render(request, "register.html", context)

def examinations(request):
    return render(request, "examinations.html",{})

def blood_tests(request):
    return render(request, "blood_tests.html",{})

def other_examinations(request):
    return render(request, "other_examinations.html",{})
