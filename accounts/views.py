from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login
from .forms import SignUpForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        # form = SignUpForm(request.POST)
        form = UserCreationForm(request.POST)
        print(form)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Logs the user in immediately after signing up
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('test')  # Change to your homepage URL
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def test_view(request):
    return render(request, 'accounts/test.html')