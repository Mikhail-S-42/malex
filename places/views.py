from django.template import loader, Context
from django.http import HttpResponse
from access.wrapper import GetAccess

@GetAccess
def PlacesList(request):
	tpl = loader.get_template('tpl.html')
	context = {'app': 'places'}
	return HttpResponse(tpl.render(context))