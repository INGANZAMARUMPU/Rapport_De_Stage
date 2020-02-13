from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path("", views.commercial, name='commercial'),
    path("<place_id>", views.commercial, name='commercial'),
    path("payer/<table_id>", views.payer, name='cpayer'),
    path("stock/", views.stock, name='cstock'),
    path("achats/<product_id>", views.achats, name='cachats'),
    path("details/<product_id>", views.details, name='cdetails'),
    path("offre/<product_id>", views.offre, name='coffre'),
]
