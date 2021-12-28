from django.template import loader, Context
from django.http import HttpResponse
from access.wrapper import GetAccess

@GetAccess
def Warehouse(request):
	tpl = loader.get_template('tpl.html')
	context = {'app': 'ppu'}
	return HttpResponse(tpl.render(context))