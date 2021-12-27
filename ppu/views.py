from django.template import loader, Context
from django.http import HttpResponse

def Warehouse(request):
	tpl = loader.get_template('tpl.html')
	context = {'app': 'ppu'}
	return HttpResponse(tpl.render(context))