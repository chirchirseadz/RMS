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