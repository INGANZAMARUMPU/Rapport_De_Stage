from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [

    path("", views.manager, name="manager"),
    path("personnel/", views.personnel, name="mpersonnel"),
    path("stock/", views.stock, name="mstock"),
    path("achats/", views.achats, name="machats"),
    path("feedbacks/", views.feedbacks, name="mfeedbacks"),
    path("recettes/", views.recettes, name="mrecettes"),
     
]
