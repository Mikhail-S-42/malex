from django.template import loader, Context
from django.http import HttpResponse
from access.wrapper import GetAccess

@GetAccess
def DataList(request):
	tpl = loader.get_template('tpl.html')
	context = {'app': 'violations'}
	return HttpResponse(tpl.render(context))