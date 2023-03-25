# forms.py
from django import forms
from .models import RentPayments

class RentPaymentsForm(forms.ModelForm):
    class Meta:
        model = RentPayments
        fields = ['year','month',]
