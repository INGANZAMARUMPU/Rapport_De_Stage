from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def manager(request):
	return render(request, 'manager/index.html', locals())
