from django.urls import include, path

urlpatterns = [
    path('', include('account.urls')),
    path('access/', include('access.urls')),
    path('devices/', include('devices.urls')),
    path('filePlaces/', include('filePlaces.urls')),
    path('loadViolations/', include('loadViolations.urls')),
    path('places/', include('places.urls')),
    path('ppu/', include('ppu.urls')),
    path('transports/', include('transports.urls')),
    path('violations/', include('violations.urls')),
]