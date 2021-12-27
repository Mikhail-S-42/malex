from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.DataList, name='DataList'),
]