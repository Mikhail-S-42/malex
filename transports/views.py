from django.template import loader, Context
from django.http import HttpResponse

def DataList(request):
	tpl = loader.get_template('tpl.html')
	context = {'app': 'transports'}
	return HttpResponse(tpl.render(context))