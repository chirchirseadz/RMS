from django.contrib import admin
from . models import Rooms, Apartments, Category, Navigation, Slider, Contacts
from dashboard.models import RoomBooking

# Register your models here.

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(Apartments, ApartmentAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
    
admin.site.register(Category, CategoryAdmin)


class AdminHouses(admin.ModelAdmin):
    list_display = ['apartment','house_number', 'house_type', 'house_description', 'price', 'add_date', 'booked', 'paid']
admin.site.register(Rooms, AdminHouses)



# class AdminSlider(admin.ModelAdmin):
#     list_display = []

admin.site.register(Slider)


class AdminContacts(admin.ModelAdmin):
    list_display = ['email', 'phone', 'location']
admin.site.register(Contacts, AdminContacts)


class AdminNavigation(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Navigation, AdminNavigation )



admin.site.register(RoomBooking)







# admin.site.register(Bookings)
