from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from . serializers import *

# Create your views here.
class ProduitViewset(viewsets.ModelViewSet):
	queryset = Produit.objects.all()
	serializer_class = ProduitSerializer

class StockViewset(viewsets.ModelViewSet):
	queryset = Stock.objects.all()
	serializer_class = StockSerializer

class AchatViewset(viewsets.ModelViewSet):
	queryset = Achat.objects.all()
	serializer_class = AchatSerializer

class FournisseurViewset(viewsets.ModelViewSet):
	queryset = Fournisseur.objects.all()
	serializer_class = FournisseurSerializer

class IngredientViewset(viewsets.ModelViewSet):
	queryset = Ingredient.objects.all()
	serializer_class = IngredientSerializer

class RecetteViewset(viewsets.ModelViewSet):
	queryset = Recette.objects.all()
	serializer_class = RecetteSerializer

class ClientViewset(viewsets.ModelViewSet):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

class RepasViewset(viewsets.ModelViewSet):
	queryset = Repas.objects.all()
	serializer_class = RepasSerializer

class PanierViewset(viewsets.ModelViewSet):
	queryset = Panier.objects.all()
	serializer_class = PanierSerializer

class CommandeViewset(viewsets.ModelViewSet):
	queryset = Commande.objects.all()
	serializer_class = CommandeSerializer

class PaiementViewset(viewsets.ModelViewSet):
	queryset = Paiement.objects.all()
	serializer_class = PaiementSerializer

class FeedBackViewset(viewsets.ModelViewSet):
	queryset = FeedBack.objects.all()
	serializer_class = FeedBackSerializer