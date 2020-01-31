from django.shortcuts import render
from apps.base.models import *
from apps.base.decorators import allowed_users

@allowed_users(groups=['table'])
def table(request, id_categorie=None): # id_categorie
	if id_categorie:
		recettes = Recettes.objects.filter(categorie__id=id_categorie)
	else:
		recettes = Recettes.objects.all()
	commande = Commande.objects.filter(client=request.user.personnel).last()
	n_carts = Panier.objects.filter(commande=commande).count()
	return render(request, 'table/index.html', locals())

@allowed_users(groups=['table'])
def feedback(request):
	return render(request, 'table/feeds.html', locals())

@allowed_users(groups=['table'])
def cart(request):
	return render(request, 'table/panier.html', locals())