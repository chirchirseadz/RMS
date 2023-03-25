from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .models import RentPayments
from users.models import UserProfile
from .forms import RentPaymentsForm


# Create your views here.
cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'

@login_required(login_url='login')
@csrf_exempt
def stk_push_success(request):
    tenant = request.user
    phone_number = tenant.userprofile.phone
    room = tenant.userprofile.room
    amount = room.price
    account_reference = f'Accura Management {tenant.userprofile.room}'
    transaction_desc = f'Rent payment for {tenant.userprofile.room}'
    callback_url = stk_push_callback_url

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

                return HttpResponse('Confirmation info is sent !!! ')
            else:
                # STK push failed, update transaction status and save it
                transaction.status = 'FAILED'
                transaction.save()

                return redirect('failure_page')

    else:
        form = RentPaymentsForm()

    context = {
        'form': form
    }

    return render(request, 'rents.html', context)


# # from django.views.decorators.csrf import csrf_exempt
# # from django.http import HttpResponse
# # from .models import RentPayments

# @csrf_exempt
# def stk_push_callback(request):
#     if request.method == 'POST':
#         # Extract data from the request
#         transaction_id = request.POST.get('TransID')
#         phone_number = request.POST.get('MSISDN')
#         amount = request.POST.get('TransAmount')
#         account_reference = request.POST.get('BillRefNumber')
#         transaction_date = request.POST.get('TransTime')

#         # Update the transaction record with the STK push details
#         try:
#             transaction = RentPayments.objects.get(transaction_id=transaction_id)
#             transaction.phone_number = phone_number
#             transaction.amount = amount
#             transaction.account_reference = account_reference
#             transaction.transaction_date = transaction_date
#             transaction.status = 'COMPLETED'
#             transaction.save()
#         except RentPayments.DoesNotExist:
#             # Handle the case where the transaction ID is not found
#             pass

#     # Return an empty response
#     return HttpResponse('')
