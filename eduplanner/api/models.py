from django.db import models
from .events import *
from core.models import *

# test model
class Response(models.Model):
    status      = models.IntegerField(default=200)
    message     = models.CharField(max_length=4096, default="")

class Event(models.Model):
    name            = models.CharField(max_length=256, default="Evento")
    description     = models.CharField(max_length=2048, default="")
    date_start      = models.CharField(max_length=16, default="1970-1-1")
    date_end        = models.CharField(max_length=16, default="1970-1-1") # make sure to handle if these two are the same
    forced          = models.BooleanField(default=False)
    event_type      = models.CharField(max_length=256, choices=eventTypes) # event type (theres like 20 of em i'll list them out later)
    admin           = models.ForeignKey(User, on_delete=models.CASCADE, default=None) # admin that added the event