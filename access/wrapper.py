from django.core.exceptions import PermissionDenied
from account.models import Profile
from .models import Access

#--------------------------------------------------------
# Декаратор для реализации доступа к приложениям.
def GetAccess(function):
	def wrapper(request):
		request.user._profile = __GetProfileUser__(request)
		if(not request.user.is_authenticated): raise PermissionDenied
		app = request.resolver_match.route.strip('/')
		if(not app in request.user._profile.listAccess): raise PermissionDenied
		return function(request)
	return wrapper

#--------------------------------------------------------
# Декаратор для проверки только автоизации.

def IsAuth(function):
	def wrapper(request):
		request.user._profile = __GetProfileUser__(request)
		if(not request.user.is_authenticated): raise PermissionDenied
		return function(request)
	return wrapper

#--------------------------------------------------------
# Функция получения группы пользователя.

def __GetProfileUser__(request): 
	profile = Profile.objects.get(user=request.user.id)
	profile.flagStart = request.session.get('_startAuth', False)
	profile.startUrl = 'account'
	profile.listAccess = list()
	__GetAccessData__(profile)
	return profile

#--------------------------------------------------------
# Функция получения группы пользователя.

def __GetAccessData__(profile):
	access = Access.objects.get(group=profile.group)
	profile.startUrl = access.startUrl
	if(access.access): profile.listAccess.append('access')
	if(access.devices): profile.listAccess.append('devices')
	if(access.places): profile.listAccess.append('places')
	if(access.violations): profile.listAccess.append('violations')
	if(access.transports): profile.listAccess.append('transports')
	if(access.ppu): profile.listAccess.append('ppu')
	if(access.loadViolations): profile.listAccess.append('loadViolations')
	if(access.filePlaces): profile.listAccess.append('filePlaces')