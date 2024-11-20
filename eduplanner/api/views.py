from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import *
from core.models import user
from .serializers import *

import os, json

# http response codes
# 200 = OK
# 403 = forbidden
# 404 = come on. you know what that one is
# 409 = conflict

# generate session token
def __gen_token():
    return os.urandom(16).hex()

# verify account
def __verify_account(request):
    # check if client token exists before indexing because otherwise it throws a fit like a baby
    server_token = user.objects.filter(session_token=request.session.get("token")) and user.objects.filter(session_token=request.session.get("token")).values()[0].get("session_token")
    local_token = request.session.get("token")

    # verify if token is valid
    return server_token and local_token and (server_token == local_token)

# Create your views here.

# view set test class
class IntegerViewSet(viewsets.ModelViewSet):
    serializer_class = ResponseSerializer
    queryset = Response.objects.all()

    def create(self, request): # POST
        serializer = ResponseSerializer(Response(
            status=200,
            message=request.POST.get("value")
        ))
        
        return HttpResponse(JSONRenderer().render(serializer.data))
    
class RegisterViewSet():
    a = 0 # stfu

class LoginViewSet():
    a = 0
