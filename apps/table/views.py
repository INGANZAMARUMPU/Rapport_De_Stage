from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from apps.base.models import *
from apps.base.decorators import allowed_users

@allowed_users(groups=['table'])
def table(request, id_categorie=None): # id_categorie
	table = get_object_or_404(Table, user=request.user)
	commande = Commande.objects.get_or_create(table=table,\
	 commandee=False, servi=False, pret=False)[0]
	categories = Categorie.objects.all()
	if id_categorie:
		recettes = Recette.objects.filter(categorie__id=id_categorie)
	else:
		recettes = Recette.objects.all()
	if request.POST.get('recette_id'):
		to_cart = Recette.objects.get(id = int(request.POST.get('recette_id')))
		panier = Panier(commande=commande, recette=to_cart, quantite=1)
		try:
			panier.save()
			messages.success(request, str(panier.recette)+" au panier")
		except IntegrityError:
			messages.success(request, str(panier.recette)+" déjà au panier")
			
	cart_rec_ids = Panier.objects.filter(commande=commande).values_list('recette', flat=True)
	n_carts = cart_rec_ids.count()
	return render(request, 'table/index.html', locals())

@allowed_users(groups=['table'])
def feedback(request):
	table = get_object_or_404(Table, user=request.user)
	commande = Commande.objects.get_or_create(table=table,\
	 commandee=False, servi=False, pret=False)[0]
	categories = Categorie.objects.all()
	carts = Panier.objects.filter(commande=commande)
	n_carts = carts.count()
	commandes = Commande.objects.filter(table=table,\
	commandee=True, servi=True, pret=True)
	paniers = Panier.objects.filter(commande__in=commandes)
	return render(request, 'table/feeds.html', locals())

@allowed_users(groups=['table'])
def cart(request):
	table = get_object_or_404(Table, user=request.user)
	commande = Commande.objects.get_or_create(table=table,\
	 commandee=False, servi=False, pret=False)[0]
	categories = Categorie.objects.all()
	carts = Panier.objects.filter(commande=commande)
	n_carts = carts.count()
	prix_total = commande.a_payer
	return render(request, 'table/panier.html', locals())