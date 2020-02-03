from .models import *
from rest_framework import serializers

class ProduitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Produit
		fields = "__all__"

class StockSerializer(serializers.ModelSerializer):
	class Meta:
		model = Stock
		fields = "__all__"

class FournisseurSerializer(serializers.ModelSerializer):
	class Meta:
		model = Fournisseur
		fields = "__all__"

class IngredientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ingredient
		fields = "__all__"

class RecetteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recette
		fields = "__all__"

class PanierSerializer(serializers.ModelSerializer):
	class Meta:
		model = Panier
		fields = "__all__"

class CommandeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Commande
		fields = "__all__"

class PaiementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Paiement
		fields = "__all__"

class FeedBackSerializer(serializers.ModelSerializer):
	class Meta:
		model = FeedBack
		fields = "__all__"
