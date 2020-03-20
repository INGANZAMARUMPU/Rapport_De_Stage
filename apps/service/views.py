from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.base.models import *

@login_required
def service(request, place_id=None, ordered=None):
	if place_id:
		places = Place.objects.filter(id=place_id)
	else:
		places = Place.objects.all()
		place_id = places.first().id;
	if places:
		tables = Table.objects.filter(place=place_id)
	return render(request, 'service/index.html', locals())

@login_required
def commandes(request, table_id):
	commandes = Commande.objects.filter(table=table_id, payee__lt=1, commandee=True)
	print(commandes)
	return render(request, 'service/commandes.html', locals())
	
