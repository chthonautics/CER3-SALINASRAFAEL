from rest_framework import routers, serializers
from .models import *
from core.models import *

# Create your models here.
class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ["status", "message"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ["name", "email", "staff"]