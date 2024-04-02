from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # logging in users 
    if request.method == 'POST':
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
            return redirect('home')
    else:
        return render(request=request, template_name='home.html', context={})
