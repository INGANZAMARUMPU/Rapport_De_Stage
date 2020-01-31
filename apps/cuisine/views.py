from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def cuisine(request):
	return render(request, 'cuisine/index.html', locals())
	
@login_required
def tables(request):
	return render(request, '404.html', locals())
	
