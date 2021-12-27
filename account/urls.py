from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as viewsAuth
from . import views


urlpatterns = [
	path('', viewsAuth.LoginView.as_view(), name='login'),
	path('logout/', viewsAuth.LogoutView.as_view(), name='logout'),
	path('account/', views.Profile, name='Profile'),
	path('account/db/', admin.site.urls),
]