from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path("", views.cuisine, name="cuisine"),
    path("tables", views.tables, name="ctables"),
]
