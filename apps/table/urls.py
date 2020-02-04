from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.table, name='table'),
    path('<int:id_categorie>', views.table, name='table'),
    path('panier/', views.cart, name='tpanier'),
    path('feedback/', views.feedback, name='tfeeds'),
]
