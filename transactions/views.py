from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

def house_bookings(request):
    cl = MpesaClient()
    # This is the mobile number which will be prompted 
    phone_number = '0790651941'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request): 
        data = request.body

        return HttpResponse('STK push in django was a success')
        # You can do whatever you want with the notification received from MPESA here.

