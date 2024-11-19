from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import *
from .serializers import *

import os, json

# http response codes
# 200 = OK
# 403 = forbidden
# 404 = come on. you know what that one is
# 409 = conflict

# Create your views here.
def integer(request):
    value = request.POST.get("value")

    # test serialization, time to understand how this works later on

    testvalue = Response(
        status=200,
        message=value
    )

    testserial = ResponseSerializer(testvalue)

    testjson = JSONRenderer().render(testserial.data)

    return HttpResponse(testjson)