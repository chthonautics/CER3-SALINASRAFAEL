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
        model = User
        fields = ["name", "email", "staff"]

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "name", "description", "date_start", "date_end", "forced", "event_type"]