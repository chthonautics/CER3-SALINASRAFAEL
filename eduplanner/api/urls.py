from django.contrib import admin
from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register()

urlpatterns = [
    path('integer/', views.integer, name="integer"),
]
