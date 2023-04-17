import requests
import json

url = 'https://4efa-41-89-240-109.eu.ngrok.io/rents/pay/rent/call_back'

data = {
    "Body": {
        "stkCallback": {
            "MerchantRequestID": "12345",
            "CheckoutRequestID": "67890",
            "ResultCode": 0,
            "ResultDesc": "The service was accepted successfully",
            # add any other relevant data here
        }
    }
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.text)






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

