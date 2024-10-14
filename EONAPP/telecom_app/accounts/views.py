from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader

# Register View
def register(request):
    errors = []
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # Manual validation
        if password != password_confirm:
            errors.append("Passwords do not match.")
        if User.objects.filter(username=username).exists():
            errors.append("Username is already taken.")
        if User.objects.filter(email=email).exists():
            errors.append("Email is already in use.")

        # If no errors, save the user
        if not errors:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')

    return render(request, 'register.html', {'errors': errors})


# Login View
def login_view(request):
    errors = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('telemarket_data')  # Redirect to a home page after login
        else:
            errors.append('Invalid username or password')

    return render(request, 'login.html', {'errors': errors})

from .forms import TelemarketDataForm

# Telemarket Data Form View
def telemarket_data(request):
    if request.method == 'POST':
        form = TelemarketDataForm(request.POST)
        if form.is_valid():
            telemarket_data = form.save(commit=False)
            telemarket_data.user = request.user  # Link data to logged-in user
            telemarket_data.save()

            # TODO: Save data to Google Sheets

            return redirect('success')  # Redirect to a success page after submission
    else:
        form = TelemarketDataForm()
    return render(request, 'telemarket_data.html', {'form': form})

def success(request):
    return render(request, 'success.html')


# views.py

def home(request):
    return render(request, 'index.html')



