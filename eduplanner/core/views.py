from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import *
from .models import *

import json

# verify account
def __verify_account(request):
    # check if client token exists before indexing because otherwise it throws a fit like a baby
    server_token = User.objects.filter(session_token=request.session.get("token")) and User.objects.filter(session_token=request.session.get("token")).values()[0].get("session_token")
    local_token = request.session.get("token")

    # verify if token is valid
    return server_token and local_token and (server_token == local_token)

# Create your views here.
def index(request):
    data = {}

    if(not __verify_account(request)):
        return redirect("/login")
    else:
        return redirect("/calendar")

def calendar(request):
    if(not __verify_account(request)):
        return redirect("/login")
    
    data = {}

    return render(request, 'calendar.html', data)

def manage(request):
    if(not __verify_account(request)):
        return redirect("/login")
    
    session = User.objects.filter(session_token=request.session.get("token")).values()[0]

    # cant manage anything if not staff
    if(not session.get("staff")):
       return redirect("/")

    data = {'form': eventform}

    return render(request, 'manage.html', data)

def login(request):
    data = {'form': loginform()}

    return render(request, 'login.html', data)

def register(request):
    data = {'form': registerform()}

    return render(request, 'register.html', data)

def account(request):
    if(not __verify_account(request)):
        return redirect("/login")
    
    session = User.objects.filter(session_token=request.session.get("token")).values()[0]

    data = {
        'id'    : session.get("id"),
        'name'  : session.get("name"),
        'email' : session.get("email"),
        'staff' : session.get("staff")
    }

    return render(request, 'account.html', data)