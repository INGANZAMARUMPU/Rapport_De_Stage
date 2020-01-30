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

class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = "__all__"

class AchatForm(forms.ModelForm):
	class Meta:
		model = Achat
		fields = "__all__"

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

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
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
