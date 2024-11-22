from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128, unique=True)
    staff = models.BooleanField(default=False)
    password_sha256 = models.CharField(max_length=64)
    session_token = models.CharField(max_length=32)