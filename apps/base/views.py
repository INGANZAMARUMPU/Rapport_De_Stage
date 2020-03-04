from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from django.http import HttpResponse
from .forms import *
from .decorators import allowed_users

def disconnect(request):
	show_hidden = "hidden"
	logout(request)
	return redirect(connect)

def connect(request):
	show_hidden = "hidden"
	formulaire = ConnexionForm(request.POST)
	try:
		next_p = request.GET["next"]
	except:
		next_p = ""
	if request.method == "POST" and formulaire.is_valid():
		username = formulaire.cleaned_data['username']
		password = formulaire.cleaned_data['password']
		user = authenticate(username=username, password=password)
		if user:  # Si l'objet renvoyé n'est pas None
			login(request, user)
			messages.success(request, "You're now connected!")
			if next_p:
				return redirect(next_p)
			else:
				return redirect(index)
		# elif password.len() < 6:
		# 	messages.error(request, "Wrong password!")
		else:
			messages.error(request, "logins incorrect!")
	formulaire = ConnexionForm()
	return render(request, 'login.html', locals())

@login_required
def index(request):
	user_groups = request.user.groups.all()
	if user_groups:
		for group in user_groups:
			return rediriger(request, group.name)
	messages.error(request, 'vous avez aucune permission')
	return redirect(disconnect)

@login_required
def rediriger(request, name):
	if name == "admin":
		return redirect('manager')
	return redirect(name)
