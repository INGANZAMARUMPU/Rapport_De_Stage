from django.contrib import admin
from .models import *

class PersonnelAdmin(admin.ModelAdmin):
	list_display = ("user", "tel", "avatar")
	list_filter = ("user", "tel")
	search_field = ("user", "tel")
	ordering = ("user", "tel")

class ProduitAdmin(admin.ModelAdmin):
	list_display = ("nom", "unite_entrant", "unite_sortant", "rapport")
	list_filter = ("nom", "unite_entrant", "unite_sortant", "rapport")
	search_field = ("nom", "unite_entrant", "unite_sortant", "rapport")
	ordering = ("nom", "unite_entrant", "unite_sortant", "rapport")

class StockAdmin(admin.ModelAdmin):
	list_display = ('produit', 'quantite')
	list_filter = ('produit', 'quantite')
	search_field = ('produit', 'quantite')
	ordering = ('produit', 'quantite')

class OffreAdmin(admin.ModelAdmin):
	list_display = ('produit', 'fournisseur', "prix")
	list_filter = ('produit', 'fournisseur', "prix")
	search_field = ('produit', 'fournisseur', "prix")
	ordering = ('produit', 'fournisseur', "prix")

class AchatsAdmin(admin.ModelAdmin):
	list_display = ("produit", "quantite", "offre", "personnel", "date")
	list_filter = ("produit", "quantite", "offre", "personnel", "date")
	search_field = ("produit", "quantite", "offre", "personnel", "date")
	ordering = ("produit", "quantite", "offre", "personnel", "date")

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

class RecetteAdmin(admin.ModelAdmin):
	list_display = ("nom", "temp", "prix")
	list_filter = ("nom", "temp", "prix")
	search_field = ("nom", "temp", "prix")
	ordering = ("nom", "temp", "prix")

class ClientAdmin(admin.ModelAdmin):
	list_display = ("user", "points", "avatar",)
	list_filter = ("points", "avatar", "user")
	search_field = ("points", "avatar", "user")
	ordering = ("points", "avatar", "user")

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
admin.site.register(Achat, AchatsAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recette, RecetteAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Panier, PanierAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Commande, CommandeAdmin)
admin.site.register(Paiement, PaiementAdmin)
admin.site.register(FeedBack, FeedBackAdmin)
admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Offre, OffreAdmin)