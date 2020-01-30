from django.shortcuts import render
from .models import *

def manager(request):
	return render(request, 'manager/index.html', locals())

def personnel(request):
	return render(request, 'manager/personnel.html', locals())
	
def stock(request):
	return render(request, 'manager/stock.html', locals())
	
def achats(request):
	return render(request, 'manager/achats.html', locals())
	
def feedbacks(request):
	return render(request, 'manager/feeds.html', locals())
	
def feedDel(request):
	return render(request, 'manager/404.html', locals())
	
def recettes(request):
	return render(request, 'manager/recettes.html', locals())
