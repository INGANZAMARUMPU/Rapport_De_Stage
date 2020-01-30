from django.urls import path, include
from rest_framework import routers
from . import views, admin_views, service_views
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
    path("service/", service_views.service, name="service"),
    path("service/commandes", service_views.sCommandes, name="scommandes"),
    path("service/preparations", service_views.sPreparations, name="spreparations"),
    path("service/prepared", service_views.sPrepared, name="sprepared"),
    path("service/recettes", service_views.sRecettes, name="srecettes"),
    path("service/tables", service_views.sTables, name="stables"),

    path("manager/", admin_views.manager, name="manager"),
    path("manager/mpersonnel/", admin_views.mPersonnel, name="mpersonnel"),
    path("manager/mstock/", admin_views.mStock, name="mstock"),
    path("manager/machats/", admin_views.mAchats, name="machats"),
    path("manager/mfeedbacks/", admin_views.mFeedbacks, name="mfeedbacks"),
    path("manager/mrecettes/", admin_views.mRecettes, name="mrecettes"),
     
    path("commercial/", views.commercial, name="commercial"),
]
