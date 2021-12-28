from django.template import loader, Context
from django.http import HttpResponse
from .wrapper import GetAccess

@GetAccess
def SetPriv(request):
	tpl = loader.get_template('tpl.html')
	context = {'app': 'access'}
	return HttpResponse(tpl.render(context))
