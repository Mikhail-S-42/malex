from django.template import loader, Context
from django.http import HttpResponse

def Generate(request):
	tpl = loader.get_template('tpl.html')
	context = {'app': 'filePlaces'}
	return HttpResponse(tpl.render(context))