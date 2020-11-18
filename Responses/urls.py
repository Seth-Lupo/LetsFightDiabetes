from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path("1", views.responses1, name="1"),
    path("2", views.responses2, name="2"),
    path("3", views.responses3, name="3"),
    path("4", views.responses4, name="4"),

]