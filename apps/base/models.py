from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from datetime import datetime, timedelta
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

class Produit(models.Model):
	nom = models.CharField(max_length=64, unique=True)
	unite = models.CharField(max_length=64, verbose_name='unité de mesure')
	unite_sortant = models.CharField(max_length=64, null=True,blank=True)
	rapport = models.FloatField(default=1)

	def __str__(self):
		return self.nom

class Stock(models.Model):
	produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
	offre = models.ForeignKey("Offre", null=True, on_delete=models.SET_NULL)
	quantite = models.FloatField()
	date = models.DateField(blank=True, default=timezone.now)
	expiration = models.IntegerField(verbose_name="délais de validité(en jours)")
	expiration_date = models.DateField(editable=False)
	personnel = models.ForeignKey("Personnel", null=True, on_delete=models.SET_NULL)

	def save(self, *args, **kwargs):
		self.expiration_date=self.date+timedelta(days=self.expiration)
		super(Stock, self).save(*args, **kwargs)

class Offre(models.Model):
	produit = models.ForeignKey("Produit", null=True, on_delete=models.SET_NULL)
	fournisseur = models.ForeignKey("Fournisseur", null=True, on_delete=models.SET_NULL)
	prix = models.FloatField()

	def __str__(self):
		return f"{self.produit.nom} - {self.fournisseur}"

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
	temp = models.IntegerField(verbose_name='temp de cuisson(en minutes)')
	prix = models.IntegerField()
	image = models.ImageField(upload_to="recettes/")
	categorie = models.ForeignKey("Categorie", null=True, on_delete=models.SET_NULL)
	disponibles = models.IntegerField(verbose_name="quantité dispo")
	details = models.URLField(null=True, blank=True)

	def __str__(self):
		return f"{self.nom} à {self.prix}"

	@staticmethod
	def aleat():
		return randint(0, 1)

class Panier(models.Model):
	commande = models.ForeignKey("Commande", null=True, on_delete=models.CASCADE)
	recette = models.ForeignKey("Recette", null=True, on_delete=models.SET_NULL)
	quantite = models.IntegerField(default=1)
	somme = models.IntegerField(blank=True, verbose_name='à payer')
	pret = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		old = Panier.objects.filter(commande=self.commande, recette=self.recette)
		if old and self.quantite:
			last = old.last()
			last.quantite+=self.quantite
			self = last
		self.somme = self.recette.prix*self.quantite
		super(Panier, self).save(*args, **kwargs)


	def __str__(self):
		return f"{self.recette}"

class Commande(models.Model):
	client = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
	tel = models.CharField(verbose_name='numero de télephone', blank=True, default=0, max_length=24)
	date = models.DateField(blank=True, default=timezone.now)
	servi = models.BooleanField(default=False)
	commandee = models.BooleanField(default=False)
	pret = models.BooleanField(default=False)
	a_payer = models.FloatField(default=0, blank=True)
	payee = models.FloatField(default=0, blank=True)
	reste = models.FloatField(default=0, blank=True)

	def save(self, *args, **kwargs):
		super(Commande, self).save(*args, **kwargs)

class Paiement(models.Model):
	commande = models.ForeignKey("Commande", null=True, on_delete=models.SET_NULL)
	somme = models.IntegerField(verbose_name='somme payée', default=0)
	date = models.DateField(blank=True, default=timezone.now)

	def save(self, *args, **kwargs):
		commande = self.commande
		super(Paiement, self).save(*args, **kwargs)
		paiements = Paiement.objects.filter(commande=commande).aggregate(Sum("somme"))["somme__sum"]
		commande.payee = paiements
		commande.reste = commande.a_payer-paiements
		commande.save()

class FeedBack(models.Model):
	client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	recette = models.ForeignKey("Recette", null=True, on_delete=models.SET_NULL)
	stars = models.IntegerField()
	commentaire = models.TextField()
	visible = models.BooleanField(default=True)
	date = models.DateField(blank=True, default=timezone.now)

	class Meta:
		unique_together = ('client', 'recette')

def delZeroQuantity(sender, instance, *args, **kwargs):
	self = instance
	if not self.quantite:
		commande = self.commande
		self.delete()
		paniers = Panier.objects.filter(commande=commande)
		if not paniers:
			commande.delete()
	else:
		somme_comandes = Panier.objects.filter(commande=self.commande).aggregate(Sum('somme'))['somme__sum']
		self.commande.a_payer = somme_comandes
		self.commande.save()

# def addIfExist(sender, instance, *args, **kwargs):
# 	self = instance


post_save.connect(delZeroQuantity, sender=Panier)
# pre_save.connect(addIfExist, sender=Panier)