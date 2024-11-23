from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('integer', IntegerViewSet)
router.register('user', UserViewSet)
router.register('event', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
