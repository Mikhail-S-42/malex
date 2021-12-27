from django.template import loader, Context
from django.http import HttpResponse

def Profile(request):
	tpl = loader.get_template('tpl.html')
	context = {'app': 'account',}
	return HttpResponse(tpl.render(context))
