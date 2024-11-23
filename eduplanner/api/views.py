from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import *
from core.models import User
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
    user = User.objects.filter(session_token=request.session.get("token"))

    server_token = user and user.values()[0].get("session_token")
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
    queryset = User.objects.none() # avoid data leaks (hopefully)
    
    def create(self, request): # login/register user
        data = request.POST

        # because of le backwards compatibility i cant use match
        if(data.get("type") == "login"): 
            # reject request if no email is provided (probably vulnerable otherwise) or the password is wrong
            if(
                (not User.objects.filter(email=data.get("email"))) or
                data.get("password") != User.objects.get(email=data.get("email")).password_sha256
            ):
                return HttpResponse(status=403)

            token = gen_token()
            request.session["token"] = token

            session = User.objects.get(email=data.get("email"))
            session.session_token = token
            session.save()

            return HttpResponse(status=200)
        
        elif(data.get("type") == "register"):
            # if account already exists
            if(User.objects.filter(email=request.POST.get("email"))):
                return HttpResponse(status=409)
            
            token = gen_token()

            User(
                name            = data.get("name"),
                email           = data.get("email"),
                staff           = False, # not staff by default
                password_sha256 = data.get("password"),
                session_token   = token
            ).save()

            request.session["token"] = token

            return HttpResponse(status=200)
        
        else:
            return HttpResponse(status=404)
    
    def update(self, request, pk=None): # logout (for now)
        data = request.data # data passed by put url is currently unused because im just using the names for now
        
        if(not verify_account(request)):
            return HttpResponse(status=403)
        
        session = User.objects.get(session_token=request.session.get("token"))
        session.session_token = ""
        session.save()

        del request.session["token"]

        return HttpResponse(status=200)
    
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def create(self, request): # POST
        data = request.POST
        user = User.objects.filter(session_token=request.session.get("token"))

        # verify identity before doing anything
        if(
            (not verify_account(request))
            or (not user.values()[0].get("staff"))
        ):
            return HttpResponse(status=403)
        
        print(data, data.get("forced"))

        Event(
            name            = data.get("name"),
            description     = data.get("description"),
            date_start      = data.get("date_start"),
            date_end        = data.get("date_end"),
            forced          = data.get("forced") == "on",
            event_type      = data.get("event_type")
        ).save()

        return HttpResponse(status=200)