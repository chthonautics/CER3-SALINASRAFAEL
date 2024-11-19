from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import *

# Create your views here.
def index(request):
    data = {'form': testform()}

    return render(request, 'testpage.html', data)