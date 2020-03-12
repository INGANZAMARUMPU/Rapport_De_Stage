from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from datetime import datetime, timedelta, date
from random import randint

class Personnel(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
	tel = models.CharField(verbose_name='numero de télephone', max_length=24)

	class Meta:
		unique_together = ('tel', 'user')

	def __str__(self):
		string = self.user.first_name+self.user.last_name
		string = string if string else self.user.username
		return f"{string}"

class Image(models.Model):
	schema1 = models.ImageField(upload_to="logo/")
	schema2 = models.ImageField(upload_to="logo/")

class Place(models.Model):
	nom = models.CharField(max_length=32)

	def __str__(self):
		return self.nom

class Table(models.Model):
	user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE, unique=True)
	place = models.ForeignKey('Place', null=True, blank=True, on_delete=models.SET_NULL)
	image = models.ForeignKey('Image', null=True, blank=True, on_delete=models.SET_NULL)
	x = models.IntegerField(default=0)
	y = models.IntegerField(default=0)

	def __str__(self):
		return f"{self.user.username}"

class Produit(models.Model):
	nom = models.CharField(max_length=64, unique=True)
	unite = models.CharField(max_length=64, verbose_name='unité de mesure')
	unite_sortant = models.CharField(max_length=64, null=True,blank=True)
	rapport = models.FloatField(default=1)

	def __str__(self):
		return self.nom

	def quantiteEnStock(self):
		stocks = Stock.objects.filter(produit=self,
			is_valid=True)
		quantite = stocks.aggregate(Sum('quantite'))['quantite__sum']
		try:
			return int(quantite)
		except:
			return 0

	class Meta:
		ordering = ["nom"]

class Stock(models.Model):
	produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
	offre = models.ForeignKey("Offre", blank=True, null=True, on_delete=models.SET_NULL)
	quantite = models.FloatField()
	date = models.DateField(blank=True, default=timezone.now)
	expiration = models.PositiveIntegerField(null=True, verbose_name="délais de validité(en jours)")
	expiration_date = models.DateField(editable=False, null=True)
	personnel = models.ForeignKey("Personnel", default=1, on_delete=models.SET_DEFAULT)
	is_valid = models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		if self.expiration:
			self.expiration_date=self.date+timedelta(days=self.expiration)
		super(Stock, self).save(*args, **kwargs)

	class Meta:
		ordering = ["produit"]

class Offre(models.Model):
	produit = models.ForeignKey("Produit", null=True, on_delete=models.SET_NULL)
	fournisseur = models.ForeignKey("Fournisseur", null=True, on_delete=models.SET_NULL)
	prix = models.FloatField()

	def __str__(self):
		return f"{self.produit.nom} - {self.fournisseur} - {self.prix}"

	class Meta:
		unique_together = ('produit', 'fournisseur', 'prix')

class Fournisseur(models.Model):
	nom = models.CharField(verbose_name='nom et prenom', max_length=64)
	adresse = models.CharField(max_length=64)
	tel = models.CharField(verbose_name='numero de télephone', max_length=24)

	class Meta:
		unique_together = ('adresse', 'tel')
	def __str__(self):
		return f"{self.nom}"

class Ingredient(models.Model):
	produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
	quantite = models.FloatField()

	class Meta:
		unique_together = ('produit', 'quantite')

	def __str__(self):
		return f"{self.produit} - {self.quantite}"

class Categorie(models.Model):
	nom = models.CharField(max_length=32)

	def __str__(self):
		return f"{self.nom}"

class Nutriment(models.Model):
	recette = models.OneToOneField("Recette", null=True, on_delete=models.CASCADE)
	energy_kcal = models.FloatField(null=True, blank=True)
	protein_g = models.FloatField(null=True, blank=True)
	fat_g = models.FloatField(null=True, blank=True)
	calicium_mg = models.FloatField(null=True, blank=True)
	copper_mg = models.FloatField(null=True, blank=True)
	iodine_Mg = models.FloatField(null=True, blank=True)
	iron_mg = models.FloatField(null=True, blank=True)
	magnesium_mg = models.FloatField(null=True, blank=True)
	selenium_Mg = models.FloatField(null=True, blank=True)
	zinc_mg = models.FloatField(null=True, blank=True)

class Vitamine(models.Model):
	recette = models.OneToOneField("Recette", null=True, on_delete=models.CASCADE)
	A = models.FloatField(null=True, blank=True)
	B1 = models.FloatField(null=True, blank=True)
	B2 = models.FloatField(null=True, blank=True)
	B3 = models.FloatField(null=True, blank=True)
	B5 = models.FloatField(null=True, blank=True)
	B6 = models.FloatField(null=True, blank=True)
	B9 = models.FloatField(null=True, blank=True)
	B12 = models.FloatField(null=True, blank=True)
	C = models.FloatField(null=True, blank=True)
	D = models.FloatField(null=True, blank=True)
	E = models.FloatField(null=True, blank=True)
	K = models.FloatField(null=True, blank=True)

class Recette(models.Model):
	nom = models.CharField(max_length=64)
	ingredient = models.ManyToManyField("Ingredient")
	temp = models.PositiveIntegerField(verbose_name='temp de cuisson(en minutes)')
	prix = models.PositiveIntegerField()
	image = models.ImageField(upload_to="recettes/")
	categorie = models.ForeignKey("Categorie", null=True, on_delete=models.SET_NULL)
	disponible = models.BooleanField(default=True)
	details = models.URLField(null=True, blank=True)

	def __str__(self):
		return f"{self.nom} à {self.prix}"

	@staticmethod
	def aleat():
		return randint(0, 1)

class Panier(models.Model):
	commande = models.ForeignKey("Commande", null=True, on_delete=models.CASCADE, related_name='details')
	recette = models.ForeignKey("Recette", null=True, on_delete=models.SET_NULL)
	quantite = models.PositiveIntegerField(default=1)
	somme = models.PositiveIntegerField(blank=True, verbose_name='à payer')
	pret = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		self.somme = self.recette.prix*self.quantite
		super(Panier, self).save(*args, **kwargs)

	class Meta:
		unique_together = ('commande','recette')
			
	def __str__(self):
		return f"{self.recette}"

class Commande(models.Model):
	table = models.ForeignKey(Table, default=1, on_delete=models.SET_DEFAULT)
	tel = models.CharField(verbose_name='numero de télephone', blank=True, default=0, max_length=24)
	date = models.DateField(blank=True, default=timezone.now)
	servi = models.BooleanField(default=False, blank=True)
	commandee = models.BooleanField(default=False, blank=True)
	pret = models.BooleanField(default=False, blank=True)
	a_payer = models.FloatField(default=0, blank=True)
	payee = models.FloatField(default=0, blank=True)
	reste = models.FloatField(default=0, blank=True)
	serveur = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

	def save(self, *args, **kwargs):
		self.reste = self.a_payer-self.payee
		super(Commande, self).save(*args, **kwargs)

	def paniers(self):
		return Panier.objects.filter(commande=self)

class Paiement(models.Model):
	commande = models.ForeignKey("Commande", null=True, on_delete=models.SET_NULL)
	somme = models.PositiveIntegerField(verbose_name='somme payée', default=0)
	date = models.DateField(blank=True, default=timezone.now)

	def save(self, *args, **kwargs):
		commande = self.commande
		super(Paiement, self).save(*args, **kwargs)
		paiements = Paiement.objects.filter(commande=commande).aggregate(Sum("somme"))["somme__sum"]
		commande.payee = paiements
		commande.reste = commande.a_payer-paiements
		commande.save()

class FeedBack(models.Model):
	recette = models.ForeignKey("Recette", on_delete=models.CASCADE)
	commande = models.ForeignKey("Commande", null=True, on_delete=models.SET_NULL)
	stars = models.PositiveIntegerField()
	commentaire = models.TextField(blank=True)
	visible = models.BooleanField(default=True)
	date = models.DateField(blank=True, default=timezone.now)

	class Meta:
		unique_together = ('commande', 'recette')

def delZeroQuantity(sender, instance, *args, **kwargs):
	self = instance
	commande = self.commande
	if not self.quantite:
		paniers = Panier.objects.filter(commande=commande)
		self.delete()
		if not paniers:
			commande.delete()

	if self.pret:
		paniers = Panier.objects.filter(commande=commande, pret=False)
		if not paniers:
			commande.pret=True

	somme_comandes = Panier.objects.filter(commande=self.commande).aggregate(Sum('somme'))['somme__sum']
	self.commande.a_payer = somme_comandes
	self.commande.save()

# def addIfExist(sender, instance, *args, **kwargs):
# 	self = instance


post_save.connect(delZeroQuantity, sender=Panier)
# pre_save.connect(addIfExist, sender=Panier)