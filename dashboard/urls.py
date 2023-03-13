from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index_page'),
    path('list/of/tenant/', views.list_of_tenants, name='list_of_tenants'),
    path('list/of/inactive/tenant/', views.list_of_in_active_tenants, name='list_of_in_active_tenants'),
    path('single/tenant/<int:id>/', views.single_tenant_view, name='single_tenant_view'),
    path('manage/tenant/<int:id>/', views.ManageTenant, name='manage_tenant'),

    # BOOKINGS

    path('booking/admin/update/<int:id>/', views.adminbookingupdate, name='booking_update'),

    # APARTMENTS ROUTES
    path('apartments/add/', views.AddApartment, name='add_apartmdent'),
    path('apartments/view/', views.ApartmentsView, name='apartment_list'),
    path('apartments/update/<int:id>', views.ApartmentUpdate, name='apartment_update'),


    # HOUSES ROUTES
    path('house/add/', views.AddHouse, name='add_house'),
    path('houses/view/', views.HousesView, name='houses_list'),
    path('house/update/<int:id>', views.HouseUpdate, name='house_update'),
    path('house/del/<int:id>', views.DelRoom, name='house_del'),
    
    

    # COMPLAINTS ROUTES
    path('tenants/make/complaints/', views.FileComplaint, name='make_complaint'),
    path('tenants/complaints/view/', views.TenantComplaints, name='complaints'),
    path('tenants/complaints/view/<int:id>/', views.TenantComplaintsUpdate, name='complaints_update'),
    
    # MAKE NOTIFICATIONS TO TENANTS
    path('make/notifications/view/', views.MessagesToTenants, name='make_notification'),
    
    



]