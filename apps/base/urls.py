from django.urls import path, include
from rest_framework import routers
from .api import *


router = routers.DefaultRouter()
router.register("produit", ProduitViewset)
router.register("stock", StockViewset)
router.register("achat", AchatViewset)
router.register("fournisseur", FournisseurViewset)
router.register("ingredient", IngredientViewset)
router.register("recette", RecetteViewset)
router.register("client", ClientViewset)
router.register("panier", PanierViewset)
router.register("commande", CommandeViewset)
router.register("paiement", PaiementViewset)
router.register("feedBack", FeedBackViewset)

urlpatterns = [
    path("api/", include(router.urls)),
]