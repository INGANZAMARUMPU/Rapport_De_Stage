from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.base.models import *

@login_required
def service(request, place_id=None, ordered=None):
	if place_id:
		places = Place.objects.filter(id=place_id)
	else:
		places = Place.objects.all()
	if places:
		tables = Table.objects.filter(place=places.first())
	return render(request, 'service/index.html', locals())

@login_required
def tables(request):
	return render(request, '404.html', locals())
	
