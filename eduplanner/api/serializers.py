from rest_framework import routers, serializers
from .models import *

# Create your models here.
class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ["status", "message"]