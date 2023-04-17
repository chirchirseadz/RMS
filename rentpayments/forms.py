# forms.py
from django import forms
from .models import RentPayments, MpesaOnlinePayments, TenantRentPayments

class RentPaymentsForm(forms.ModelForm):
    class Meta:
        model = TenantRentPayments
        fields = ['rent_details']

        labels = {
              'RentDetails': 'Select the Month you are paying for'
            }
