from .models import *
from rest_framework import serializers

class ProduitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Produit
		fields = "__all__"

class TableSerializer(serializers.ModelSerializer):
	class Meta:
		model = Table
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
	nom = serializers.SerializerMethodField()
	def get_nom(self, obj):
		return obj.recette.nom

	class Meta:
		model = Panier
		fields = "id", "quantite", "somme", "pret", "commande", "recette", 'nom', 'obligations'

class CommandeSerializer(serializers.ModelSerializer):
	details = PanierSerializer(many=True, read_only=True)
	class Meta:
		model = Commande
		fields = ("table", "details", "tel", "date", "servi", "commandee", "pret", "a_payer", "payee", "reste", "serveur")

class DeepPanierSerializer(serializers.ModelSerializer):
	class Meta:
		model = Panier
		fields = "__all__"
		depth = 1

class DeepCommandeSerializer(serializers.ModelSerializer):
	details = DeepPanierSerializer(many=True, read_only=True)
	class Meta:
		model = Commande
		fields = ("table", "details", "tel", "date", "servi", "commandee", "pret", "a_payer", "payee", "reste", "serveur")

class PaiementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Paiement
		fields = "__all__"

class FeedBackSerializer(serializers.ModelSerializer):
	class Meta:
		model = FeedBack
		fields = "__all__"
