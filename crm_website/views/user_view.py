from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

def login_user(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authentication
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.success(request, "Login Unsuccessful. Please check username and password.")
            return redirect('home')
            
        else:
            login(request, user)
            messages.success(request, "Login Successful!")
        
        return redirect('customers')
    
    except Exception as e:
        print("Cannot process login request - ", e)
        return HttpResponse("Error processing login request.", status=500)

def logout_user(request):
    try:
        logout(request)
        messages.success(request, "Logged out Successfully.")
        return redirect('home')
    
    except Exception as e:
        print("Cannot process logout request - ", e)
        return HttpResponse("Error processing logout request.", status=500)

def register_user(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if len(password) < 7:
                messages.error(request, "Password must be atleast 8 characters long.")
                return redirect('register')

            if password != confirm_password:
                messages.error(request, "Passwords do not match")
                return redirect('register')
            
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists. Proceed to Login.")
                return redirect('register')

            # Create user
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password)  # Hash the password
            )

            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            return render(request, 'register.html')

    except Exception as e:
        return HttpResponse("Error processing register user request.", status=500)