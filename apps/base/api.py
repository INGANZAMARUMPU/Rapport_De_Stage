from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import render
from django.db.models import F

from .models import *
from .serializers import *

# Create your views here.
class ProduitViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Produit.objects.all()
	serializer_class = ProduitSerializer

class StockViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Stock.objects.all()
	serializer_class = StockSerializer

	@action(methods=['GET'], detail=False,
		url_path=r'quantite/(?P<product_id>[0-9]+)',
		url_name="quantite_total")
	def quantiteTotal(self, request, product_id):
		stocks = Stock.objects.filter(produit=product_id)
		somme = stocks.aggregate(Sum('quantite'))['quantite__sum']
		return Response({'quantite':somme})

class FournisseurViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Fournisseur.objects.all()
	serializer_class = FournisseurSerializer

class IngredientViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Ingredient.objects.all()
	serializer_class = IngredientSerializer

class RecetteViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Recette.objects.all()
	serializer_class = RecetteSerializer

class PanierViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Panier.objects.all()
	serializer_class = PanierSerializer

	@action(methods=["PUT"],
		url_path=r"payer/(?P<table_id>[0-9]+)/(?P<somme>[0-9]+)",
		url_name="api_payer", detail=False)
	def payement(self, request, table_id, somme):
		somme = int(somme)
		commandes = Commande.objects.filter(table=table_id, commandee=True, reste__gt=0)
		print(commandes)
		a_payer = None
		for commande in commandes:
			if somme >= commande.reste:
				somme -= commande.reste
				Paiement(commande=commande, somme=commande.reste).save()
			elif somme >= 0:
				Paiement(commande=commande, somme=somme).save()
				somme = 0
				a_payer = commande.reste
				break
		return Response({'reste':a_payer})

class DeepPanierViewSet(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Panier.objects.all()
	serializer_class = DeepPanierSerializer

	@action(methods=["GET"],
		url_path=r"commande/(?P<commande_id>[0-9]+)",
		url_name="cart_by_commande", detail=False)
	def byCommande(self, request, commande_id):
		queryset = Panier.objects.filter(commande=commande_id, pret=False)
		serializer = DeepPanierSerializer(queryset, many=True)
		return Response(serializer.data)

class CommandeViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Commande.objects.all()
	serializer_class = CommandeSerializer

	@action(methods=['get'], detail=False, \
		url_path=r'(?P<table_id>[0-9]+)/commands_count',\
		url_name='table_commands_count')
	def nTableCom(self, request, table_id):
		table = Table.objects.get(id=table_id)
		total = Commande.objects.filter(table=table, commandee=True, servi=False)
		already = total.filter(serveur__isnull=True)
		return Response({"total":total.count(), "to_serve":already.count()})

	@action(methods=['get'], detail=False, \
		url_path=r'(?P<place_id>[0-9]+)/place_comands_count',\
		url_name='place_comands_count')
	def nPlaceCom(self, request, place_id):
		# place = Place.objects.get(id=place_id)
		tables = Table.objects.filter(place=place_id)
		total = Commande.objects.filter(table__in=tables, commandee=True, payee=False)
		already = Commande.objects.filter(table__in=tables, commandee=True, payee=False, serveur__isnull=True)
		return Response({"total":total.count(), "to_serve":already.count()})

	@action(methods=['get'], detail=False,
		url_path=r'(?P<table_id>[0-9]+)/all_commands',
		url_name='table_commands')
	def TableCom(self, request, table_id):
		table = Table.objects.get(id=table_id)
		queryset = Commande.objects.filter(table=table, commandee=True, payee=False)
		serializer = CommandeSerializer(queryset, many=True)
		return Response(serializer.data)

class PaiementViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Paiement.objects.all()
	serializer_class = PaiementSerializer

class FeedBackViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = FeedBack.objects.all()
	serializer_class = FeedBackSerializer

class TableViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Table.objects.all()
	serializer_class = TableSerializer