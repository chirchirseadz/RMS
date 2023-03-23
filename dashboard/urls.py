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
    path('apartments/delete/<int:id>', views.DeleteApartment, name='apartment_delete'),


    # HOUSES ROUTES
    path('house/add/', views.AddHouse, name='add_house'),
    path('houses/view/', views.HousesView, name='houses_list'),
    path('house/update/<int:id>', views.HouseUpdate, name='house_update'),
    path('house/del/<int:id>', views.DelRoom, name='house_del'),
    
    # CREATE CATEGORIES
    
    path('create/category/', views.AddCategory, name='add_category'),
    path('categories/view/', views.categories, name='categories'),
    path('categories/delete/<int:id>/', views.DeleteCategory, name='delete_category'),

    #  ALLOCATE ROOM ROUTES
    path('allocate/room/', views.AllocateRoom, name='disallocate_room'),


    # COMPLAINTS ROUTES
    path('tenants/make/complaints/', views.FileComplaint, name='make_complaint'),
    path('tenants/complaints/view/', views.TenantComplaints, name='complaints'),
    path('tenants/complaints/view/<int:id>/', views.TenantComplaintsUpdate, name='complaints_update'),
    
    # MAKE NOTIFICATIONS TO TENANTS
    path('make/notifications/view/', views.MessagesToTenants, name='make_notification'),
    

    # SLIDER ROUTES

    path('make/slider/', views.createslider, name='create_slider'),
    path('View/slider/', views.viewsliders, name='view_slider'),
    path('del/slider/<int:id>/', views.deleteslider, name='del_slider'),
    path('update/slider/<int:id>', views.updateslider, name='update_slider'),

    
    # CONTACTS ADD
    path('make/contact/', views.create_contacts, name='create_contact'),
    path('view/contact/', views.view_contacts, name='view_contact'),
    path('del/contact/<int:id>/', views.delete_contacts, name='delete_contact'),

]