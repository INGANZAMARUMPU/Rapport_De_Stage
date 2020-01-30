from django.shortcuts import render
from .models import *

def service(request):
	return render(request, 'service/index.html', locals())

def preparations(request):
	return render(request, 'service/preparations.html', locals())
	
def prepared(request):
	return render(request, 'service/prepared.html', locals())

def recettes(request):
	return render(request, 'service/recettes.html', locals())

def tables(request):
	return render(request, '404.html', locals())
	
