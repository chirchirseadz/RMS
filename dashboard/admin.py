from django.contrib import admin
from . models import *

# Register your models here.
class AdminMessage(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message','message_date']
admin.site.register(MessagesFromTenants, AdminMessage)


class AdminNotices(admin.ModelAdmin):
    list_display = ['subject', 'message', 'notice_date']
admin.site.register(NoticesToTenants, AdminNotices)


admin.site.register(Complaints)
admin.site.register(AllocateRoom)