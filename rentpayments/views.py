from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .models import RentPayments, MpesaOnlinePayments, RentDetails, TenantRentPayments
from users.models import UserProfile
from .forms import RentPaymentsForm
from django.contrib import messages

import json

# Create your views here.
cl = MpesaClient()
# stk_callback_url = 'https://api.darajambili.com/express-payment'
stk_callback_url = 'https://54a7-41-89-240-109.eu.ngrok.io/rents/pay/rent/call_back'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'
    
@login_required(login_url='login')
@csrf_exempt



def stk_push_success(request):

    try: 
        tenant = request.user.userprofile
        phone_number = tenant.phone
        room = tenant.room
        # amount = room.price
        amount = 1
        account_reference = f'Accura Management {tenant.room}'
        transaction_desc = f'Rent payment for {tenant.room}'
        callback_url = stk_callback_url
    except:
        messages.warning(request, 'You have not been assigned a room. contact Management via the contacts page !!')
        return redirect('pay_rent')
  
    if request.method == 'POST':
        form = RentPaymentsForm(request.POST)
        if form.is_valid():
            # Create a new RentPayments object but don't save it yet
        
            transaction = form.save(commit=False)
            transaction.tenant = tenant
            transaction.room = room
            transaction.phone_number = phone_number
            transaction.amount = room.price
            transaction.account_reference = account_reference
            transaction.transaction_desc = transaction_desc
            transaction.callback_url = callback_url
            
            # Send STK push request and handle response
            try:
                transaction.save()
            except:
                messages.warning(request, ' You have already paid For the selected Mounth !!')
                return redirect('pay_rent')
         
            response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
           
            data = (response)
            print(f'this is the data ===== > {data}')
            
            if response.status_code == 200:
                # STK push successful, update transaction status and save it
                transaction.MerchantRequestID = response.json()['MerchantRequestID']
                transaction.CheckoutRequestID = response.json()['CheckoutRequestID']
                data = response.json()
                print(f' This is the data ===== > {data}')
                transaction.save()
                messages.success(request, 'Confirmation info is sent to your handset. Enter Your pin !!! ')
                return redirect('pay_rent')
            else:
                # STK push failed, update transaction status and save it
                messages.warning(request, 'Not able to pay rents. Kindly contact Management !!')
                return redirect('pay_rent')
    
        messages.success(request, 'Rents Payed !!!!')
        return redirect('index_page')
    else:
        form = RentPaymentsForm()

    context = {
        'form': form
    }

    return render(request, 'rents/payrents.html', context)




@csrf_exempt
def stk_push_callback(request):
    get_body = request.body
    data = json.loads(get_body)
    print(data)
    return_data = data['Body']['stkCallback']
    
    try:
        transaction_id = return_data['CheckoutRequestID']
        
         # Retrieve the transaction object
        transaction = TenantRentPayments.objects.get(CheckoutRequestID=transaction_id)


        started_pay = MpesaOnlinePayments.objects.get(
            CheckoutRequestID=return_data['CheckoutRequestID'],
        ) 
        started_pay.tenant = transaction.userprofile
        started_pay.Room = request.user.userprofile.room
        started_pay.MerchantRequestID = return_data['MerchantRequestID']
        started_pay.ResultCode = return_data['ResultCode']
        started_pay.ResultDesc = return_data['ResultDesc']
        started_pay.Amount = return_data['CallbackMetadata']['Item'][0]['Value']
        started_pay.MpesaReceiptNumber = return_data['CallbackMetadata']['Item'][1]['Value']
        started_pay.TransactionDate = return_data['CallbackMetadata']['Item'][3]['Value']
        started_pay.PhoneNumber = return_data['CallbackMetadata']['Item'][4]['Value']
        started_pay.Approved = True

      
        started_pay.save()
    except ObjectDoesNotExist:
        pay = MpesaOnlinePayments(
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
    return JsonResponse(data)



# TENANTS RENTS

def Rents(request):
    return render(request, 'rents/rents.html')

def TenantsRentDetails(request):
    rents = RentDetails.objects.all()
    
    context = {'rents': rents}
    return render(request, 'rents/rentdetails.html', context)

def OnlineRents(request):
    lipa_na_mpesa_rents = MpesaOnlinePayments.objects.filter(tenant=request.user.userprofile)
    context = { 
        'lipa_na_mpesa_rents': lipa_na_mpesa_rents,
    }
    return render(request, 'rents/onlinerents.html', context)




def OfflineRents(request):
    handset_payments_rents = RentPayments.objects.all()
    context = { 
        'handset_payments_rents': handset_payments_rents
    }
    return render(request, 'rents/offlinerents.html', context)

# SINGLE RENTS

def SingleOnlineRent(request, id):
    payments = MpesaOnlinePayments.objects.get(id=id)

    context = {
        "payments": payments
    }
    return render(request, 'rents/single_online_rents.html', context)



def SingleOfflineRents(request, id):
    payments = RentPayments.objects.get(id=id)
    context = {
        'payments': payments
    }
    return render(request, 'rents/single_offline_rents.html', context)





























# def stk_push_success(request):
#     try:
#         tenant = request.user
#         phone_number = tenant.userprofile.phone
#         room = tenant.userprofile.room
#         amount = room.price
#         # amount = 1
#         account_reference = f'Accura Management {tenant.userprofile.room}'
#         transaction_desc = f'Rent payment for {tenant.userprofile.room}'
#         callback_url = stk_callback_url
#     except:
#        messages.warning(request, "You've Not been assigned a Room. Contact your Administrator !!!")
#        return redirect('index_page')

#     if request.method == 'POST':
#         form = RentPaymentsForm(request.POST)
#         if form.is_valid():
#             # Create a new RentPayments object but don't save it yet
            
#                 transaction = form.save(commit=False)
#                 transaction.tenant = tenant.userprofile
#                 transaction.room = room
#                 transaction.phone_number = phone_number
#                 transaction.amount = room.price
#                 transaction.account_reference = account_reference
#                 transaction.transaction_desc = transaction_desc
#                 transaction.callback_url = callback_url
#                 # Send STK push request and handle response
#                 response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
           
#                 if response.status_code == 200:
#                     # STK push successful, update transaction status and save it
#                     transaction.transaction_id = response.json()['MerchantRequestID']
                
#                     messages.success(request, 'Confirmation info is sent to your handset. Enter Your pin !!! ')
#                     return redirect('pay_rent')
#                 else:
#                     # STK push failed, update transaction status and save it
                    
#                     messages.warning(request, 'Not able to pay rents. Kindly contact your Land Lord !!')
#                     return redirect('pay_rent')
            
#         messages.success(request, 'Rents Payed !!!!')
#         return redirect('index_page')

#     else:
#         form = RentPaymentsForm()

#     context = {
#         'form': form
#     }

#     return render(request, 'rents/payrents.html', context)
