from django.urls import path, include
from rest_framework import routers
from .api import *
from . import views

router = routers.DefaultRouter()
router.register("produit", ProduitViewset)
router.register("stock", StockViewset)
router.register("fournisseur", FournisseurViewset)
router.register("ingredient", IngredientViewset)
router.register("recette", RecetteViewset)
router.register("panier", PanierViewset)
router.register("commande", CommandeViewset)
router.register("deep_panier", DeepPanierViewSet)
router.register("paiement", PaiementViewset)
router.register("feedBack", FeedBackViewset)
router.register("table", TableViewset)

urlpatterns = [
    path("api/", include(router.urls)),
    path("login/", views.connect, name="login"),
    path("logout/", views.disconnect, name="logout"),
    path("", views.index, name="index"),
]
