from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .models import RentPayments, MpesaOnline
from users.models import UserProfile
from .forms import RentPaymentsForm

import json

# Create your views here.
cl = MpesaClient()
# stk_callback_url = 'https://api.darajambili.com/express-payment'
stk_callback_url = 'https://54a7-41-89-240-109.eu.ngrok.io/rents/pay/rent/call_back'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'
    
@login_required(login_url='login')
@csrf_exempt
def stk_push_success(request):
    tenant = request.user
    phone_number = tenant.userprofile.phone
    room = tenant.userprofile.room
    # amount = room.price
    amount = 1
    account_reference = f'Accura Management {tenant.userprofile.room}'
    transaction_desc = f'Rent payment for {tenant.userprofile.room}'
    callback_url = stk_callback_url

    if request.method == 'POST':
        form = RentPaymentsForm(request.POST)
        if form.is_valid():
            # Create a new RentPayments object but don't save it yet
            transaction = form.save(commit=False)
            transaction.tenant = tenant.userprofile
            transaction.room = room
            transaction.phone_number = phone_number
            transaction.amount = room.price
            transaction.account_reference = account_reference
            transaction.transaction_desc = transaction_desc
            transaction.callback_url = callback_url

            # Send STK push request and handle response
            response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

            if response.status_code == 200:
                # STK push successful, update transaction status and save it
                transaction.status = 'COMPLETED'
                transaction.transaction_id = response.json()['MerchantRequestID']
                transaction.save()

                return HttpResponse('Confirmation info is sent. Enter Your pin  !!! ')
            else:
                # STK push failed, update transaction status and save it
                transaction.status = 'FAILED'
                transaction.save()

                return HttpResponse('Failed')

    else:
        form = RentPaymentsForm()

    context = {
        'form': form
    }

    return render(request, 'rents.html', context)

@csrf_exempt
def stk_push_callback(request):
    get_body = request.body
    data = json.loads(get_body)
    return_data = data['Body']['stkCallback']
    
    try:
        started_pay = MpesaOnline.objects.get(
            CheckoutRequestID=return_data['CheckoutRequestID'],
        )    
        started_pay.MerchantRequestID = return_data['MerchantRequestID']
        started_pay.ResultCode = return_data['ResultCode']
        started_pay.ResultDesc = return_data['ResultDesc']
        started_pay.Amount = return_data['CallbackMetadata']['Item'][0]['Value']
        started_pay.MpesaReceiptNumber = return_data['CallbackMetadata']['Item'][1]['Value']
        started_pay.TransactionDate = return_data['CallbackMetadata']['Item'][3]['Value']
        started_pay.PhoneNumber = return_data['CallbackMetadata']['Item'][4]['Value']
        started_pay.save()
    except ObjectDoesNotExist:
        pay = MpesaOnline(
            MerchantRequestID = return_data['MerchantRequestID'],
            CheckoutRequestID = return_data['CheckoutRequestID'],
            ResultCode = return_data['ResultCode'],
            ResultDesc = return_data['ResultDesc'],
            Amount = return_data['CallbackMetadata']['Item'][0]['Value'],
            MpesaReceiptNumber = return_data['CallbackMetadata']['Item'][1]['Value'],
            TransactionDate = return_data['CallbackMetadata']['Item'][3]['Value'],
            PhoneNumber = return_data['CallbackMetadata']['Item'][4]['Value'],
            )
        pay.save()

    context = {
        "status": "completed",
    }
    return JsonResponse(dict(context))



# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponseBadRequest

# @csrf_exempt
# def stk_push_callback(request):
#     if request.method == 'GET':
#         # Extract the transaction details from the request
#         transaction_id = request.GET.get('TransactionID')
#         phone_number = request.GET.get('MSISDN')
#         amount = request.GET.get('TransAmount')
#         result_code = request.GET.get('ResultCode')
#         result_desc = request.GET.get('ResultDesc')

#         # Perform any necessary validation on the transaction details
#         if result_code != '0':
#             return HttpResponseBadRequest('Transaction failed: {}'.format(result_desc), result_code)

#         # Create a new instance of the transaction model and save it to the database
#         transaction = MpesaOnline.objects.create(
#             MerchantRequestID=transaction_id,
#             PhoneNumber=phone_number,
#             Amount=amount,
#             ResultCode=result_code,
#             ResultDesc=result_desc,
#         )
#         transaction.save()

#         # Return a success response to the M-PESA server
#         return HttpResponse('Transaction saved successfully')
#     else:
#         return HttpResponseBadRequest('Invalid request method')


