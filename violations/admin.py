from django.contrib import admin
from .models import Archive, ErrorType, Error

admin.site.register(Archive)
admin.site.register(ErrorType)
admin.site.register(Error)
