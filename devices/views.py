from django.template import loader, Context
from django.http import HttpResponse

def DevList(request):
	tpl = loader.get_template('tpl.html')
	context = {'app': 'devices'}
	return HttpResponse(tpl.render(context))
