from django import forms
from dashboard.models import RoomBooking


class RoomBookingForm(forms.ModelForm):
    requested_by = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your name'}))
    email= forms.CharField(widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email'}))
    phone_number = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'(xxx)xxx-xxxx'}))
    request_info= forms.CharField(widget= forms.Textarea
                           (attrs={'placeholder':'Describe Your Request'}))
    class Meta:
        model = RoomBooking
        fields = ['requested_by', 'email', 'phone_number', 'request_info', ]

        labels = {
                'requested_by': 'Your Names'
            }

class AdminBookingUpdateForm(forms.ModelForm):

    class Meta:
        model = RoomBooking
        fields = ['status']
