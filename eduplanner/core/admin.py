from django.contrib import admin
from api.models import *
from .models import *

# Register your models here.
admin.site.register(Response)
admin.site.register(User)
admin.site.register(Event)