from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def manager(request):
	return render(request, 'manager/index.html', locals())

@login_required
def personnel(request):
	return render(request, 'manager/personnel.html', locals())

@login_required	
def stock(request):
	return render(request, 'manager/stock.html', locals())

@login_required	
def achats(request):
	return render(request, 'manager/achats.html', locals())

@login_required	
def feedbacks(request):
	return render(request, 'manager/feeds.html', locals())

@login_required	
def feedDel(request):
	return render(request, 'manager/404.html', locals())

@login_required	
def recettes(request):
	return render(request, 'manager/recettes.html', locals())
