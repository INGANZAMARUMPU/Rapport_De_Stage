from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import render
from django.db.models import F

from .models import *
from django.contrib.auth.models import Group
from datetime import date, timedelta, datetime
from .serializers import *
from django.db.models import Count

# Create your views here.
class ChartServiceViewset(viewsets.ViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]

	@action(methods=['GET'], detail=False, url_name="chart_service",
		url_path=r'servicedu(?P<debut>(\d{1,4}[-]?){3})au(?P<fin>(\d{1,4}[-]?){3})', )
	def servicedetail(self, request, debut, fin):
		service = Group.objects.get(name='service')
		serveurs = User.objects.filter(groups__in=[service])

		fin = datetime.strptime(fin, "%Y-%m-%d")
		debut = datetime.strptime(debut, "%Y-%m-%d")
		delta = fin - debut
		data, labels, datasets = {}, [], []
		for a in range(delta.days+1):
			date = debut + timedelta(days=a)
			labels.append(date.strftime("%Y-%m-%d"))
		data['labels'] = labels
		for serveur in serveurs:
			services = []
			for date in labels:
				service = Commande.objects.filter(
					serveur=serveur, date= date).values('serveur', 'date')\
					.annotate(Count('pk'))
				if service:
					services.append(service[0]["pk__count"])
				else:
					services.append(0)
			datasets.append({'label':serveur.username, 'data':services})
		
		data['datasets'] = datasets
		return Response(data)

	@action(methods=['GET'], detail=False, url_path=r'service', url_name="chart_service_detail")
	def service(self, request):
		fin = datetime.today()
		debut = fin - timedelta(days=7)
		fin = fin.strftime("%Y-%m-%d")
		debut = debut.strftime("%Y-%m-%d")
		return self.servicedetail(request, debut, fin)

	@action(methods=['GET'], detail=False, url_name="groupe_service",
		url_path=r'servicegroupesdu(?P<debut>(\d{1,4}[-]?){3})au(?P<fin>(\d{1,4}[-]?){3})', )
	def servicegroupe(self, request, debut, fin):
		service = Group.objects.get(name='service')
		serveurs = User.objects.filter(groups__in=[service])
		labels, data = [], []
		for serveur in serveurs:
			commandes = Commande.objects.filter(date__gte=debut, serveur=serveur, date__lte=fin)\
				.values('serveur').annotate(Count('serveur'))
			labels.append(serveur.username)
			if commandes:
				data.append(commandes[0]["serveur__count"])
			else:
				data.append(0)

		print(labels, data)
		return Response({'labels':labels, 'data':data})

	@action(methods=['GET'], detail=False, url_name="groupe_service_default",
		url_path=r'servicegroupesdefault', )
	def servicegroupedefault(self, request):
		fin = datetime.today()
		debut = fin - timedelta(days=20)
		fin = fin.strftime("%Y-%m-%d")
		debut = debut.strftime("%Y-%m-%d")
		return self.servicegroupe(request, debut, fin)

class ChartEnteeSortie(viewsets.ViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]

	@action(methods=['GET'], detail=False, url_name="chart_es",
		url_path=r'esdu(?P<debut>(\d{1,4}[-]?){3})au(?P<fin>(\d{1,4}[-]?){3})', )
	def esdetail(self, request, debut, fin):
		fin = datetime.strptime(fin, "%Y-%m-%d")
		debut = datetime.strptime(debut, "%Y-%m-%d")
		delta = fin - debut
		entree, sortie, labels= [], [], []
		for i in range(delta.days+1):
			date = debut + timedelta(days=i)
			labels.append(date.strftime("%Y-%m-%d"))
			service = Commande.objects.filter(
				payee__gt=0, date= date).aggregate(Sum('payee'))
			stock = Stock.objects.filter(quantite__gt=0, date=date).annotate(
			montant=F('quantite')*F('offre__prix')).aggregate(Sum("montant"))
			if service["payee__sum"]:
				entree.append(service["payee__sum"])
			else:
				entree.append(0)
			if stock["montant__sum"]:
				sortie.append(stock["montant__sum"])
			else:
				sortie.append(0)
		return Response({
			'labels':labels,
			"datasets":[
				{'label':"entree", 'data':entree},
				{'label':"sortie", 'data':sortie}
			]})

	@action(methods=['GET'], detail=False, url_name="bar_es",
		url_path=r'esbardu(?P<debut>(\d{1,4}[-]?){3})au(?P<fin>(\d{1,4}[-]?){3})', )
	def esbar(self, request, debut, fin):
		fin = datetime.strptime(fin, "%Y-%m-%d")
		debut = datetime.strptime(debut, "%Y-%m-%d")
		labels = ['entree', 'sortie', 'perte']
		data= []
		service = Commande.objects\
			.filter(payee__gt=0, date__gte=debut, date__lte=fin)\
			.aggregate(entree=Sum('payee'))
		
		stock = Stock.objects\
			.filter(quantite__gt=0, date__gte=debut, date__lte=fin)\
			.annotate(montant=F('quantite')*F('offre__prix'))\
			.aggregate(sortie=Sum("montant"))

		data.append(service['entree'])
		data.append(stock['sortie'])
		data.append(0)
		return Response({
			'labels':labels,
			"datasets":[
				{'data':data},
			]})

	@action(methods=['GET'], detail=False, url_name="chart_es_default",
		url_path=r'esdefault', )
	def esdefault(self, request):
		fin = datetime.today()
		debut = fin - timedelta(days=20)
		fin = fin.strftime("%Y-%m-%d")
		debut = debut.strftime("%Y-%m-%d")
		return self.esdetail(request, debut, fin)

	@action(methods=['GET'], detail=False, url_name="bar_es_default",
		url_path=r'esbardefault', )
	def esbardefault(self, request):
		fin = datetime.today()
		debut = fin - timedelta(days=20)
		fin = fin.strftime("%Y-%m-%d")
		debut = debut.strftime("%Y-%m-%d")
		return self.esbar(request, debut, fin)

class ChartMode(viewsets.ViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]

	@action(methods=['GET'], detail=False, url_name="chart_mode",
		url_path=r'modedu(?P<debut>(\d{1,4}[-]?){3})au(?P<fin>(\d{1,4}[-]?){3})', )
	def modedetail(self, request, debut, fin):
		fin = datetime.strptime(fin, "%Y-%m-%d")
		debut = datetime.strptime(debut, "%Y-%m-%d")
		data = []
		mode = Panier.objects\
			.filter(commande__date__lte=fin, commande__date__gte=debut)\
			.values('recette__nom').annotate(times=Count('recette__nom'))

		return Response({
			'labels': [panier['recette__nom'] for panier in mode],
			"datasets":[
				{'data':[panier['times'] for panier in mode]},
			]})

	@action(methods=['GET'], detail=False, url_name="mode_default",
		url_path=r'', )
	def modedefault(self, request):
		fin = datetime.today()
		debut = fin - timedelta(days=20)
		fin = fin.strftime("%Y-%m-%d")
		debut = debut.strftime("%Y-%m-%d")
		return self.modedetail(request, debut, fin)

class ChartFeedBack(viewsets.ViewSet):
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]

	@action(methods=['GET'], detail=True, url_name="chart_feed",
		url_path=r'feeddu(?P<debut>(\d{1,4}[-]?){3})au(?P<fin>(\d{1,4}[-]?){3})', )
	def feeddetail(self, request, pk, debut, fin):
		fin = datetime.strptime(fin, "%Y-%m-%d")
		debut = datetime.strptime(debut, "%Y-%m-%d")
		data = []
		for i in range(1, 6):
			feedback = FeedBack.objects\
			.filter(date__lte=fin, date__gte=debut, recette=pk)\
			.filter(stars=i).aggregate(note=Count('stars'))
			data.append(feedback['note'])

		return Response({
			'labels': [1, 2, 3, 4, 5],
			"datasets":[
				{'label':"stars", 'data':data},
			]})

	@action(methods=['GET'], detail=True, url_name="feed_default",
		url_path=r'feedback', )
	def feeddefault(self, request, pk):
		fin = datetime.today()
		debut = fin - timedelta(days=20)
		fin = fin.strftime("%Y-%m-%d")
		debut = debut.strftime("%Y-%m-%d")
		return self.feeddetail(request, pk, debut, fin)

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
		url_path=r'quantite/(?P<stock_id>[0-9]+)',
		url_name="quantite_total")
	def quantiteTotal(self, request, stock_id):
		# stocks = Stock.objects.filter(produit=self,
		# 	quantite__gt=0, 
		# 	expiration_date__gt=datetime.now())
		# quantite = stocks.aggregate(Sum('quantite'))['quantite__sum']
		stock = Stock.objects.get(id=stock_id)
		return Response({'quantite':stock.produit.quantiteEnStock()})

	@action(methods=["GET"],
		url_path=r"requisition/(?P<stock_id>[0-9]+)",
		url_name="api_requisition", detail=False)
	def requisition(self, request, stock_id):
		stock = Stock.objects.get(id=stock_id)
		
		if stock.quantite<stock.produit.quantiteEnStock():
			stock.is_valid = True
			stock.save()
		else:
			stock.quantite = stock.produit.quantiteEnStock()
			stock.is_valid = True
			stock.save()	
		
		return Response({"reste":stock.produit.quantiteEnStock()})

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
