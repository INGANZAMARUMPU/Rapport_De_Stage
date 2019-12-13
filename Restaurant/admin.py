from django.contrib import admin
from .models import *

# Register your models here.
class ProduitAdmin(admin.ModelAdmin):
	list_display = ("nom", "unite_entrant", "unite_sortant", "rapport", "fournisseur", "prix")
	list_filter = ("nom", "unite_entrant", "unite_sortant", "rapport", "fournisseur", "prix")
	search_field = ("nom", "unite_entrant", "unite_sortant", "rapport", "fournisseur", "prix")
	ordering = ("nom", "unite_entrant", "unite_sortant", "rapport", "fournisseur", "prix")

class StockAdmin(admin.ModelAdmin):
	list_display = ('produit', 'quantite')
	list_filter = ('produit', 'quantite')
	search_field = ('produit', 'quantite')
	ordering = ('produit', 'quantite')

class AchatsAdmin(admin.ModelAdmin):
	list_display = ("produit", "quantite", "fournisseur", "date")
	list_filter = ("produit", "quantite", "fournisseur", "date")
	search_field = ("produit", "quantite", "fournisseur", "date")
	ordering = ("produit", "quantite", "fournisseur", "date")

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
	list_display = ("tel", "user", "points", "avatar",)
	list_filter = ("points", "avatar", "tel", "user")
	search_field = ("points", "avatar", "tel", "user")
	ordering = ("points", "avatar", "tel", "user")

class RepasAdmin(admin.ModelAdmin):
	list_display = ('recette', 'quantite')
	list_filter = ('recette', 'quantite')
	search_field = ('recette', 'quantite')
	ordering = ('recette', 'quantite')

class PanierAdmin(admin.ModelAdmin):
	list_display = ("commandee", "client", "servi")
	list_filter = ("commandee", "client", "repas", "servi")
	search_field = ("commandee", "client", "repas", "servi")
	ordering = ("commandee", "client", "repas", "servi")

class CommandeAdmin(admin.ModelAdmin):
	list_display = ("panier","no_table","date","somme","payee","reste","fini")
	list_filter = ("panier","no_table","date","somme","payee","reste","fini")
	search_field = ("panier","no_table","date","somme","payee","reste","fini")
	ordering = ("panier","no_table","date","somme","payee","reste","fini")

class PaiementAdmin(admin.ModelAdmin):
	list_display = ("commande","somme","date")
	list_filter = ("commande","somme","date")
	search_field = ("commande","somme","date")
	ordering = ("commande","somme","date")

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
admin.site.register(Repas, RepasAdmin)
admin.site.register(Panier, PanierAdmin)
admin.site.register(Commande, CommandeAdmin)
admin.site.register(Paiement, PaiementAdmin)
admin.site.register(FeedBack, FeedBackAdmin)