from django.shortcuts import redirect

def allowed_users(groups=[]):
	def decorateur(fonction):
		def wrapper_fonction(request, *args, **kwargs):
			user_groups = request.user.groups.all()
			if user_groups:
				for group in user_groups:
					if group.name in groups:
						return(fonction(request, *args, **kwargs))
			return redirect('logout')
		return wrapper_fonction
	return decorateur


	