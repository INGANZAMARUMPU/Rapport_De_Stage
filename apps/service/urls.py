from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path("", views.service, name="service"),
    path("commandes/<table_id>", views.commandes, name="scommandes"),
    path("<place_id>", views.service, name="service"),
    path("<place_id>/<ordered>", views.service, name="service"),
]
