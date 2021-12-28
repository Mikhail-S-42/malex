from django.template import loader, Context
from django.shortcuts  import redirect
from django.http import HttpResponse
from access.wrapper import IsAuth
from .models import Profile

@IsAuth
def Profile(request):
	if(request.user._profile.startUrl != 'account' and not request.user._profile.flagStart):
		request.session['_startAuth'] = True
		return redirect('../%s/' % request.user._profile.startUrl)
	#
	tpl = loader.get_template('tpl.html')
	context = {'app': 'account',}
	return HttpResponse(tpl.render(context))
