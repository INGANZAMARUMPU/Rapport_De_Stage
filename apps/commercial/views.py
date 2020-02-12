from django.shortcuts import render
from django.db.models import Sum

from apps.base.models import *
from apps.base.forms import *

def loadPlaces(place_id=None):
	places = Place.objects.all()
	if place_id:
		tables = Table.objects.filter(place=place_id)
		return places, tables
	return places, []


def commercial(request, place_id=None):
	places, tables = loadPlaces(place_id)
	return render(request, 'commercial/index.html', locals())
	
def payer(request, table_id):
	table = Table.objects.get(id=table_id)
	commandes = Commande.objects.filter(table=table_id, reste__gt=0)
	a_payer = commandes.aggregate(Sum('reste'))['reste__sum']
	return render(request, 'commercial/payement.html', locals())
	
def stock(request):
	places, tables = loadPlaces()
	products = Produit.objects.all()
	return render(request, 'commercial/stock.html', locals())
	
def achats(request, product_id):
	form = StockForm(product_id, request.POST)
	if request.method == "POST":
		stock = form.save(commit=False)
		stock.personnel = request.user.personnel
		stock.save()
	form = StockForm(product_id)
	return render(request, 'commercial/achats.html', locals())

def details(request, product_id):
	stocks = Stock.objects.filter(produit = product_id)
	return render(request, 'commercial/details.html', locals())

def tables(request):
	return render(request, '404.html', locals())
	

