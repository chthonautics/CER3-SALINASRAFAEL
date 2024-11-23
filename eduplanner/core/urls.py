from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('account/', views.account, name="account"),
    path('manage/', views.manage, name="manage"),
    path('calendar/', views.calendar, name="calendar"),
]
