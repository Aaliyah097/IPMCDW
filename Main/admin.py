from django.contrib import admin
from .models import User, Industry, ViewNote

# Register your models here.

admin.site.register(User)
admin.site.register(Industry)
admin.site.register(ViewNote)
