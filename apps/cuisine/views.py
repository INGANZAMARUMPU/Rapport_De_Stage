from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.base.models import *
from apps.base.forms import RequisitionForm
from django.forms import formset_factory

@login_required
def cuisine(request):
	no_navbar = True
	commandes = Commande.objects.filter(commandee=True, pret=False, servi=False)[:10]
	return render(request, 'cuisine/index.html', locals())

@login_required
def stock(request):
	products = Produit.objects.all()
	return render(request, 'cuisine/stock.html', locals())

def details(request, produit_id):
	recettes = Recette.objects.filter(ingredient__produit__id=produit_id)
	print(recettes)
	return render(request, 'cuisine/details.html', locals())

def requisition(request):
	if request.method == "POST":
		form_set=formset_factory(RequisitionForm)
		formset=form_set(request.POST)
		if formset.is_valid():
			for form in formset:	
				produit = form.cleaned_data['produit']
				quantite = form.cleaned_data['quantite']
				Stock(produit=produit, quantite=-quantite,
					personnel=request.user.personnel,
					is_valid=False).save()
	form_set=formset_factory(RequisitionForm)
	return render(request, 'cuisine/requisition.html', locals())
	
@login_required
def tables(request):
	return render(request, '404.html', locals())
	
