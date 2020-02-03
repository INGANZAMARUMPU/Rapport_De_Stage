from django.shortcuts import render
from django.db.models import Sum
from apps.base.models import *
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
		get_or_create = Panier.objects.get_or_create(commande=commande, recette=to_cart, quantite=1)
		if not get_or_create[1]:
			panier = get_or_create[0]
			panier.quantite+=1
			panier.save()
	n_carts = Panier.objects.filter(commande=commande).count()
	return render(request, 'table/index.html', locals())

@allowed_users(groups=['table'])
def feedback(request):
	return render(request, 'table/feeds.html', locals())

@allowed_users(groups=['table'])
def cart(request):
	commande = Commande.objects.get_or_create(client=request.user,\
	 commandee=False, servi=False, pret=False)[0]
	categories = Categorie.objects.all()
	carts = Panier.objects.filter(commande=commande)
	n_carts = carts.count()
	prix_total = carts.aggregate(Sum('somme'))
	return render(request, 'table/panier.html', locals())