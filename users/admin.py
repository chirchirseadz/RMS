from django.contrib import admin
from . models import  UserProfile, CustomUser

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(UserProfile)
