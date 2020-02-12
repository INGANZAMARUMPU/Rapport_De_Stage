from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.base.models import *

@login_required
def cuisine(request):
	no_navbar = True
	commandes = Commande.objects.filter(commandee=True, pret=False, servi=False)[:10]
	return render(request, 'cuisine/index.html', locals())
	
@login_required
def tables(request):
	return render(request, '404.html', locals())
	
