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

# definitions
# POST:     create
# GET:      list
# GET:      retrieve        (pk)
# PUT:      update          (pk)
# PATCH:    partial_update  (pk)
# DELETE:   destroy         (pk)

# generate session token
def gen_token():
    return os.urandom(16).hex()

# verify account
def verify_account(request):
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
    
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = user.objects.all()
    
    def create(self, request): # register user
        data = request.POST

        # if account already exists
        if(user.objects.filter(email=request.POST.get("email"))):
            return HttpResponse(status=409)
        
        token = gen_token()

        user(
            name            = data.get("name"),
            email           = data.get("email"),
            staff           = False, # not staff by default
            password_sha256 = data.get("password"),
            session_token   = token
        ).save()

        request.session["token"] = token

        return HttpResponse(status=200)
    
    def retrieve(self, request, pk=None): # get user data
        return HttpResponse(status=200)

    def update(self, request, pk=None): # update token and whatnot
        data = request.data

        # because of le backwards compatibility i cant use match
        if(data.get("type") == "logout"):
            if(not verify_account(request)):
                return HttpResponse(status=403)
            
            session = user.objects.get(session_token=request.session.get("token"))
            session.session_token = ""
            session.save()

            del request.session["token"]
            

        return HttpResponse(status=200)