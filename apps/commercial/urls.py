from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path("", views.commercial, name='commercial'),
    path("commercial/commandes", views.commandes, name='ccommandes'),
    path("commercial/stock", views.stock, name='cstock'),
    path("commercial/achats", views.achats, name='cachats'),
    path("commercial/offres", views.offres, name='coffres'),
]
