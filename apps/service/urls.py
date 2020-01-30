from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path("", views.service, name="service"),
    path("preparations", views.preparations, name="spreparations"),
    path("prepared", views.prepared, name="sprepared"),
    path("recettes", views.recettes, name="srecettes"),
    path("tables", views.tables, name="stables"),
]
