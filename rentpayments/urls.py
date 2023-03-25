from django.urls import path
from . import views

urlpatterns = [
  path('pay/rent/', views.stk_push_success, name='pay_rent'),
  path('pay/rent/call_back', views.stk_push_callback, name='pay_rent_call_back'),

]