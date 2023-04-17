from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(RentPayments)
admin.site.register(RentDetails)
admin.site.register(MpesaOnlinePayments)
admin.site.register(Year)

admin.site.register(TenantRentPayments)