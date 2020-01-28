from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Personnel(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.ForeignKey("Role", on_delete=models.SET_NULL, null=True)
	# role = models.ManyToManyField("Role")
	avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
	tel = models.CharField(verbose_name='numero de télephone', max_length=24)

	class Meta:
		unique_together = ('tel', 'role', 'user')

	def __str__(self):
		string = self.user.first_name+self.user.last_name
		string = string if string else self.user.username
		return f"{string}"

class Role(models.Model):
	nom = models.CharField(max_length=20)
	
	def __str__(self):
		return f"{self.nom}"

class Produit(models.Model):
	nom = models.CharField(max_length=64)
	unite_entrant = models.CharField(max_length=64)
	unite_sortant = models.CharField(max_length=64)
	rapport = models.IntegerField()
	fournisseur = models.ForeignKey("Fournisseur", null=True, on_delete=models.SET_NULL)
	prix = models.IntegerField(verbose_name="prix de vente")

	def __str__(self):
		return nom

	class Meta:
		unique_together = ('nom', 'fournisseur', 'prix')

class Stock(models.Model):
	produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
	quantite = models.IntegerField()

	class Meta:
		unique_together = ('produit', 'quantite')

	def __str__(self):
		return f"{self.quantite} {self.produit.unite_entrant} de {self.produit}"

class Achat(models.Model):
	produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
	offre = models.ForeignKey("Offre", on_delete=models.CASCADE)
	quantite = models.IntegerField()
	date = models.DateField(blank=True, default=timezone.now)
	personnel = models.ForeignKey("Personnel", null=True, on_delete=models.SET_NULL)
	
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

class Ingredient(models.Model):
	produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
	quantite = models.IntegerField()

	class Meta:
		unique_together = ('produit', 'quantite')
	def __str__(self):
		return f"{self.produit} - {self.quantite}"

class Recette(models.Model):
	nom = models.CharField(max_length=32)
	ingredient = models.ManyToManyField("Ingredient")
	temp = models.IntegerField(verbose_name='temp de cuisson(en minutes)')
	prix = models.IntegerField()

	def __str__(self):
		return f"{self.nom} à {self.prix}"

class Client(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	points = models.IntegerField()
	avatar = models.ImageField(upload_to="avatars/")
	tel = models.CharField(verbose_name='numero de télephone', max_length=24)

class Repas(models.Model):
	recette = models.ForeignKey("Recette", null=True, on_delete=models.SET_NULL)
	quantite = models.IntegerField()

	class Meta:
		unique_together = ('recette', 'quantite')
		verbose_name_plural = "Repas"

class Panier(models.Model):
	client = models.ForeignKey("Client", null=True, blank=True, on_delete=models.SET_NULL)
	repas = models.ManyToManyField("Repas")
	commandee = models.BooleanField(default=False)
	servi = models.BooleanField(default=False)

class Commande(models.Model):
	panier = models.ForeignKey("Panier", null=True, on_delete=models.CASCADE)
	no_table = models.CharField(verbose_name='numero de table', max_length=16)
	date = models.DateField(blank=True, default=timezone.now)
	somme = models.IntegerField(verbose_name='à payer')
	payee = models.IntegerField(verbose_name='déjà payée', default=0)
	reste = models.IntegerField(verbose_name='reste', null=True)
	fini = models.BinaryField(default=False)

class Paiement(models.Model):
	commande = models.ForeignKey("Commande", null=True, on_delete=models.SET_NULL)
	somme = models.IntegerField(verbose_name='somme payée')
	date = models.DateField(blank=True, default=timezone.now)

class FeedBack(models.Model):
	client = models.ForeignKey("Client", null=True, on_delete=models.SET_NULL)
	recette = models.ForeignKey("Recette", null=True, on_delete=models.SET_NULL)
	stars = models.IntegerField()
	commentaire = models.TextField()
	visible = models.BooleanField(default=True)
	date = models.DateField(blank=True, default=timezone.now)

	class Meta:
		unique_together = ('client', 'recette')

def onPaiementSaved(sender, instance, *args, **kwargs):
	a_payer = instance.commande.somme
	payee = instance.commande.payee+instance.somme
	instance.commande.payee += payee
	instance.commande.reste = a_payer - payee
	if a_payer >= payee:
		instance.fini=True

post_save.connect(onPaiementSaved, sender=Paiement)