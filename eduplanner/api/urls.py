from django.contrib import admin
from django.urls import path, include
from . import views
from .views import IntegerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('integer', IntegerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
