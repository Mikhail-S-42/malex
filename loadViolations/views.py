from django.template import loader, Context
from django.http import HttpResponse

def SetData(request):
	tpl = loader.get_template('tpl.html')
	context = {'app': 'loadViolations'}
	return HttpResponse(tpl.render(context))