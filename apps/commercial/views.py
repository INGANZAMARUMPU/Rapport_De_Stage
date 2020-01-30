from django.shortcuts import render
from .models import *

def commercial(request):
	return render(request, 'commercial/index.html', locals())

def commandes(request):
	return render(request, 'commercial/commandes.html', locals())
	
def stock(request):
	return render(request, 'commercial/stock.html', locals())
	
def achats(request):
	return render(request, 'commercial/achats.html', locals())

def offres(request):
	return render(request, 'commercial/offres.html', locals())

def tables(request):
	return render(request, '404.html', locals())
	

