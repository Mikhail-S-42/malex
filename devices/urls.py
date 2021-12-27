from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.DevList, name='DevList'),
]