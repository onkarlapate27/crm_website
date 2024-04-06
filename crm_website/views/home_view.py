from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    try:
        return render(request=request, template_name='home.html', context={})
    except Exception as e:
        print("Exception occured - ", e)