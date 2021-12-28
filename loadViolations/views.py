from django.template import loader, Context
from django.http import HttpResponse
from access.wrapper import GetAccess

@GetAccess
def SetData(request):
	tpl = loader.get_template('tpl.html')
	context = {'app': 'loadViolations'}
	return HttpResponse(tpl.render(context))