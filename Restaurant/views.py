from django.shortcuts import render
from .models import *

def service(request):
	return render(request, 'index.html', locals())

def commercial(request):
	return render(request, 'commercial.html', locals())
