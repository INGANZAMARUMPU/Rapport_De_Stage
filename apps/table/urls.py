from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.table, name='table'),
    path('panier', views.feedback, name='tpanier'),
    path('panier/<id_categorie>', views.feedback, name='tpanier'),
    path('feedback', views.cart, name='tfeeds'),
]
