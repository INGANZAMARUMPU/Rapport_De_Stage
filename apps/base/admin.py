from django.contrib import admin
from .models import *

class PersonnelAdmin(admin.ModelAdmin):
	list_display = ("user", "tel", "avatar")
	list_filter = ("user", "tel")
	search_field = ("user", "tel")
	ordering = ("user", "tel")

class ProduitAdmin(admin.ModelAdmin):
	list_display = ("nom", "unite", "unite_sortant")
	list_filter = ("nom", "unite", "unite_sortant")
	search_field = ("nom", "unite", "unite_sortant")
	ordering = ("nom", "unite", "unite_sortant")

class OffreAdmin(admin.ModelAdmin):
	list_display = ('produit', 'fournisseur', "prix")
	list_filter = ('produit', 'fournisseur', "prix")
	search_field = ('produit', 'fournisseur', "prix")
	ordering = ('produit', 'fournisseur', "prix")

class StockAdmin(admin.ModelAdmin):
	list_display = ("produit", "quantite", "offre", "personnel", "date", "expiration_date")
	list_filter = ("produit", "quantite", "offre", "personnel", "date", "expiration_date")
	search_field = ("produit", "quantite", "offre", "personnel", "date", "expiration_date")
	ordering = ("produit", "quantite", "offre", "personnel", "date", "expiration_date")

class FournisseurAdmin(admin.ModelAdmin):
	list_display = ('nom', 'adresse', 'tel')
	list_filter = ('nom', 'adresse', 'tel')
	search_field = ('nom', 'adresse', 'tel')
	ordering = ('nom', 'adresse', 'tel')

class IngredientAdmin(admin.ModelAdmin):
	list_display = ('produit', 'quantite')
	list_filter = ('produit', 'quantite')
	search_field = ('produit', 'quantite')
	ordering = ('produit', 'quantite')

class NutrimentAdmin(admin.ModelAdmin):
	list_display = ("recette", "energy_kcal", "protein_g", "fat_g", "calicium_mg", "copper_mg", "iodine_Mg", "iron_mg", "magnesium_mg", "selenium_Mg", "zinc_mg")
	list_filter = ("recette", "energy_kcal", "protein_g", "fat_g", "calicium_mg", "copper_mg", "iodine_Mg", "iron_mg", "magnesium_mg", "selenium_Mg", "zinc_mg")
	search_field = ("recette", "energy_kcal", "protein_g", "fat_g", "calicium_mg", "copper_mg", "iodine_Mg", "iron_mg", "magnesium_mg", "selenium_Mg", "zinc_mg")
	ordering = ("recette", "energy_kcal", "protein_g", "fat_g", "calicium_mg", "copper_mg", "iodine_Mg", "iron_mg", "magnesium_mg", "selenium_Mg", "zinc_mg")

class VitamineAdmin(admin.ModelAdmin):
	list_display = ("recette", "A", "B1", "B2", "B3", "B5", "B6", "B9", "B12", "C", "D", "E", "K")
	list_filter = ("recette", "A", "B1", "B2", "B3", "B5", "B6", "B9", "B12", "C", "D", "E", "K")
	search_field = ("recette", "A", "B1", "B2", "B3", "B5", "B6", "B9", "B12", "C", "D", "E", "K")
	ordering = ("recette", "A", "B1", "B2", "B3", "B5", "B6", "B9", "B12", "C", "D", "E", "K")

class RecetteAdmin(admin.ModelAdmin):
	list_display = ("nom", "temp", "image", "prix", "details")
	list_filter = ("nom", "temp", "image", "prix", "details")
	search_field = ("nom", "temp", "image", "prix", "details")
	ordering = ("nom", "temp", "image", "prix", "details")

class PanierAdmin(admin.ModelAdmin):
	list_display = ("commande", "recette", "quantite", "somme", "pret")
	list_filter = ("commande", "recette", "quantite", "somme", "pret")
	search_field = ("commande", "recette", "quantite", "somme", "pret")
	ordering = ("commande", "recette", "quantite", "somme", "pret")

class CommandeAdmin(admin.ModelAdmin):
	list_display = ("client", "tel", "date", "servi", "commandee", "pret")
	list_filter = ("client", "tel", "date", "servi", "commandee", "pret")
	search_field = ("client", "tel", "date", "servi", "commandee", "pret")
	ordering = ("client", "tel", "date", "servi", "commandee", "pret")

class PaiementAdmin(admin.ModelAdmin):
	list_display = ("commande","somme","date")
	list_filter = ("commande","somme","date")
	search_field = ("commande","somme","date")
	ordering = ("commande","somme","date")

class CategorieAdmin(admin.ModelAdmin):
	list_display = ("nom",)
	list_filter = ("nom",)
	search_field = ("nom",)
	ordering = ("nom",)

class FeedBackAdmin(admin.ModelAdmin):
	list_display = ("client", "recette", "stars", "commentaire", "visible", "date")
	list_filter = ("client", "recette", "stars", "commentaire", "visible", "date")
	search_field = ("client", "recette", "stars", "commentaire", "visible", "date")
	ordering = ("client", "recette", "stars", "commentaire", "visible", "date")


admin.site.register(Produit, ProduitAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recette, RecetteAdmin)
admin.site.register(Panier, PanierAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Commande, CommandeAdmin)
admin.site.register(Paiement, PaiementAdmin)
admin.site.register(FeedBack, FeedBackAdmin)
admin.site.register(Offre, OffreAdmin)
admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Nutriment, NutrimentAdmin)
admin.site.register(Vitamine, VitamineAdmin)
