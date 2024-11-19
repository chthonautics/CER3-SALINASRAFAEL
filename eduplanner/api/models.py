from django.db import models

class Response(models.Model):
    status = models.IntegerField(default=200)
    message = models.CharField(max_length=4096, default="")