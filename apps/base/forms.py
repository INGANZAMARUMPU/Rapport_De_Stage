from .models import *
from django import forms

class ConnexionForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username ','class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password ', 'type':'password','class':'form-control'}))

class PasswordForm(forms.Form):
	password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Password ','class':'form-control'}), label='Password')
	password2 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Confirm password ','class':'form-control'}), label='Confirm password')

class ProduitForm(forms.ModelForm):
	class Meta:
		model = Produit
		fields = "__all__"

class RequisitionForm(forms.Form):
	produits_dispo = []
	for x in Produit.objects.all():
		if x.quantiteEnStock()>0:
			produits_dispo.append(x.id)
			
	produit = forms.ModelChoiceField(
	    widget = forms.Select(
	    	attrs = {'placeholder': '', 'class': 'form-control col-12'}
	    	),
	    queryset = Produit.objects.filter(id__in=produits_dispo),
	    label = 'produit')
	quantite = forms.FloatField(
		widget=forms.NumberInput(
			attrs={'step': "0.01", 'placeholder':'quantite','class':'form-control col-12'}
			))

	# def __init__(self, *args, **kwargs):
	# 	self.produits_dispo = []
	# 	for x in Produit.objects.all():
	# 		if x.quantiteEnStock()>0:
	# 			self.produit.append(x.id)
	# 	super(RequisitionForm, self).__init__(*args, **kwargs)

class OffreForm(forms.ModelForm):
	fournisseur = forms.ModelChoiceField(
		widget = forms.Select(
			attrs={'placeholder': 'fournisseur', 'class':'form-control'}),
		queryset = Fournisseur.objects.all())
	prix = forms.CharField(
		widget=forms.NumberInput(
			attrs={'placeholder':'prix', 'class':'form-control'}))
	class Meta:
		model = Offre
		fields = ("fournisseur", "prix")

class StockForm(forms.ModelForm):
	offre = forms.ModelChoiceField(
		widget = forms.Select(
			attrs={'placeholder':'offre','class':'form-control'}),
		queryset = Offre.objects.all())
	quantite = forms.IntegerField(
		widget=forms.NumberInput(
			attrs={'placeholder':'quantite','class':'form-control'}))
	expiration = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'délais de validité(en jours)','class':'form-control'}))
	class Meta:
		model = Stock
		fields = ("offre", "quantite", "expiration")

	def __init__(self, produit_id, *args, **kwargs):
		super(StockForm, self).__init__(*args, **kwargs)
		self.base_fields["offre"].queryset = Offre.objects.filter(produit=produit_id)
		
class FournisseurForm(forms.ModelForm):
	class Meta:
		model = Fournisseur
		fields = "__all__"

class IngredientForm(forms.ModelForm):
	class Meta:
		model = Ingredient
		fields = "__all__"

class RecetteForm(forms.ModelForm):
	nom = forms.CharField(
		widget=forms.TextInput(
			attrs={'placeholder':'Nom de la recette ','class':'form-control'}
		), 
		label='Nom'
	)
	temp = forms.CharField(
		widget=forms.TextInput(
			attrs={'placeholder':'durée de cuisson','class':'form-control'}
		), 
		label='durée'
	)
	prix = forms.IntegerField(
		widget=forms.NumberInput(
			attrs={'placeholder':'prix de vente ','class':'form-control'}
		), 
		label='prix'
	)
	ingredient = forms.ModelMultipleChoiceField(
		widget = forms.Select(attrs = {'placeholder': '', 'class': 'form-control'}),
		queryset = Ingredient.objects.all()
	)
	class Meta:
		model = Recette
		fields = "__all__"

class PanierForm(forms.ModelForm):
	class Meta:
		model = Panier
		fields = "__all__"

class CommandeForm(forms.ModelForm):
	class Meta:
		model = Commande
		fields = "__all__"

class PaiementForm(forms.ModelForm):
	class Meta:
		model = Paiement
		fields = "__all__"

class FeedBackForm(forms.ModelForm):
	class Meta:
		model = FeedBack
		fields = "__all__"
