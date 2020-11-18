from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path("", views.home, name="HOME"),
    path("1", views.article1, name="1"),
    path("2", views.article2, name="2"),
    path("3", views.article3, name="3"),
    path("4", views.article4, name="4"),
    path("citations", views.citations, name="CITATIONS"),

]