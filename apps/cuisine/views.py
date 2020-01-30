from django.shortcuts import render
from .models import *

def cuisine(request):
	return render(request, 'cuisine/index.html', locals())

def tables(request):
	return render(request, '404.html', locals())
	
