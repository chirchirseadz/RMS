from django.urls import path
from . import views

urlpatterns = [
  path('pay/rent/', views.stk_push_success, name='pay_rent'),
  path('pay/rent/call_back', views.stk_push_callback, name='pay_rent_call_back'),

# TENANTS RENTS DETAILS ROUTES
  path('rents/', views.Rents, name='rents'),
  path('rents/details/', views.TenantsRentDetails, name='rents_details'),
  path('online/rent/list/', views.OnlineRents, name='online_rent_list'),
  path('offline/rent/list/', views.OfflineRents, name='offline_rent_list'),

  path('single/online/rent/list/<int:id>/', views.SingleOnlineRent, name='single_online_rent'),
  path('single/offline/rent/list/<int:id>/', views.SingleOfflineRents, name='single_offline_rent'),

]