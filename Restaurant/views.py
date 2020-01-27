from django.shortcuts import render
from .models import *

def service(request):
	return render(request, 'service.html', locals())

def manager(request):
	return render(request, 'manager.html', locals())

def commercial(request):
	return render(request, 'commercial.html', locals())
