from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path("", views.service, name="service"),
    path("<place_id>", views.service, name="service"),
    path("<place_id>/<ordered>", views.service, name="service"),
    path("tables", views.tables, name="stables"),
]
