from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path("", views.cuisine, name="cuisine"),
    path("stock", views.stock, name="cuistock"),
    path("details/<produit_id>", views.details, name="cuidetails"),
    path("requisition", views.requisition, name="cuirequisition"),
    path("tables", views.tables, name="ctables"),
]
