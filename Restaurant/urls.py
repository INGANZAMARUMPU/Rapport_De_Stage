from django.urls import path, include
from rest_framework import routers
from . import views, admin_views
from .api import *


router = routers.DefaultRouter()
router.register("produit", ProduitViewset)
router.register("stock", StockViewset)
router.register("achat", AchatViewset)
router.register("fournisseur", FournisseurViewset)
router.register("ingredient", IngredientViewset)
router.register("recette", RecetteViewset)
router.register("client", ClientViewset)
router.register("repas", RepasViewset)
router.register("panier", PanierViewset)
router.register("commande", CommandeViewset)
router.register("paiement", PaiementViewset)
router.register("feedBack", FeedBackViewset)

urlpatterns = [
    path("api/", include(router.urls)),
    path("service/", views.service, name="service"),

    path("manager/", admin_views.manager, name="manager"),
    path("manager/mpersonnel/", admin_views.mPersonnel, name="mpersonnel"),
    path("manager/mpersonnel/add/", admin_views.mPersAdd, name="mpers_add"),
    path("manager/mpersonnel/edit/<pers_id>", admin_views.mPersEdit, name="mpers_edit"),
    path("manager/mpersonnel/del/<pers_id>", admin_views.mPersDel, name="mperso_del"),
    path("manager/mstock/", admin_views.mStock, name="mstock"),
    path("manager/machats/", admin_views.mAchats, name="machats"),
    path("manager/mfeedbacks/", admin_views.mFeedbacks, name="mfeedbacks"),
    path("manager/mfeedbacks/del/<feed_id>", admin_views.mFeedDel, name="mfeed_del"),
    path("manager/mrecettes/", admin_views.mRecettes, name="mrecettes"),
    path("manager/mrecettes/add", admin_views.mRecAdd, name="mrec_add"),
    path("manager/mrecettes/edit/<rec_id>", admin_views.mRecEdit, name="mrec_edit"),
    path("manager/mrecettes/del/<rec_id>", admin_views.mRecDel, name="mrec_del"),
    
    path("commercial/", views.commercial, name="commercial"),
]
