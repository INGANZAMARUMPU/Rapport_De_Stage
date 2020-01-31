from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def service(request):
	return render(request, 'service/index.html', locals())

@login_required
def preparations(request):
	return render(request, 'service/preparations.html', locals())

@login_required	
def prepared(request):
	return render(request, 'service/prepared.html', locals())

@login_required
def recettes(request):
	return render(request, 'service/recettes.html', locals())

@login_required
def tables(request):
	return render(request, '404.html', locals())
	
