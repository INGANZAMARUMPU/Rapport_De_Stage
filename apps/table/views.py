from django.shortcuts import render
from apps.base.models import *
from django.contrib import messages
from apps.base.decorators import allowed_users

@allowed_users(groups=['table'])
def table(request, id_categorie=None): # id_categorie
	commande = Commande.objects.get_or_create(client=request.user,\
	 commandee=False, servi=False, pret=False)[0]
	categories = Categorie.objects.all()
	if id_categorie:
		recettes = Recette.objects.filter(categorie__id=id_categorie)
	else:
		recettes = Recette.objects.all()
	if request.POST.get('recette_id'):
		to_cart = Recette.objects.get(id = int(request.POST.get('recette_id')))
		get_or_create = Panier.objects.get_or_create(commande=commande, recette=to_cart)
		panier = get_or_create[0]
		if not get_or_create[1]:
			panier.quantite+=1
			panier.save()
		messages.success(request,\
			str(panier.quantite)+" "+str(panier.recette)+" au panier")
	n_carts = Panier.objects.filter(commande=commande).count()
	return render(request, 'table/index.html', locals())

@allowed_users(groups=['table'])
def feedback(request):
	commande = Commande.objects.get_or_create(client=request.user,\
	 commandee=False, servi=False, pret=False)[0]
	categories = Categorie.objects.all()
	carts = Panier.objects.filter(commande=commande)
	n_carts = carts.count()
	commandes = Commande.objects.filter(client=request.user,\
	commandee=True, servi=True, pret=True)
	paniers = Panier.objects.filter(commande__in=commandes)
	print(paniers)
	return render(request, 'table/feeds.html', locals())

@allowed_users(groups=['table'])
def cart(request):
	commande = Commande.objects.get_or_create(client=request.user,\
	 commandee=False, servi=False, pret=False)[0]
	categories = Categorie.objects.all()
	carts = Panier.objects.filter(commande=commande)
	n_carts = carts.count()
	prix_total = commande.a_payer
	return render(request, 'table/panier.html', locals())