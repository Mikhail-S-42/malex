from django.shortcuts import render, redirect
from django.contrib import auth

# Авторизация
#-----------------------------------------------------

def auth(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = auth.authenticate(username=username, password=password)
	if(user is None or not user.is_active): return render(request,'auth.html')
	auth.login(request, user)
	return redirect('/app_malex/panel/')

#-----------------------------------------------------



# Вывод панели.
#-----------------------------------------------------	

def panel(request):
	id_form = request.POST.get('username')
	if(id_form is None): return render(request,'panel.html')
	return ajax(request, id_form)

#-----------------------------------------------------


# Обработка ajax запроса для панели.
#-----------------------------------------------------

def ajax(request, id_form): return render(request,'auth.html',context={'id_form':id_form,}) 

#-----------------------------------------------------