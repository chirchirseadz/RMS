from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.house_bookings, name='housebookings'),
    path('daraja/stk_push/', views.stk_push_callback, name='stk_push_callback'),
    
]