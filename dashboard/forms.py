from django import forms
from .models import MessagesFromTenants, AllocateRoom, NoticesToTenants, Complaints
from users.models import  UserProfile, CustomUser
from houses.models import Apartments, Rooms


class Userform(forms.ModelForm):
    firstname= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your first name'}))
    email= forms.CharField(widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email'}))
    phonenumber= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'(xxx)xxx-xxxx'}))


class ActivateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ['username', 'first_name','last_name','email','is_active',]
        widgets = {
            'start_date': forms.DateInput(),
            'end_date': forms.DateInput(),
            'due_date': forms.DateInput(),
        }

class ManageTenantForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class NoticesToTenantsForm(forms.ModelForm):
   
    
    subject= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter The Subject'}))
    message = forms.CharField(widget= forms.Textarea
                           (attrs={'placeholder':'Enter Your Message'}))
    class Meta:
        model = NoticesToTenants
        fields = [ 'subject', 'message' ]


class MessagesFromTenantsForm(forms.ModelForm):
    name= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your Name'}))
    email= forms.CharField(widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email'}))
    subject= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter The Subject'}))
    message = forms.CharField(widget= forms.Textarea
                           (attrs={'placeholder':'Enter Your Message'}))
    class Meta:
        model = MessagesFromTenants
        fields = ['name', 'email', 'subject', 'message' ]



class ComplaintsForm(forms.ModelForm):
    description = forms.CharField(widget= forms.Textarea
                           (attrs={'placeholder':'Describe Your Compaints'}))
    subject = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter Your Subject of your Compaint'}))
    class Meta:
        model = Complaints
        fields = ['priority', 'subject', 'description' ]

class AdminComplaintsForm(forms.ModelForm):
    class Meta:
            model = Complaints
            fields = ['status']

# APARTMENTS

class ApartmentAddForm(forms.ModelForm):
    name= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter Apartment Name'}))
    
    class Meta:
        model = Apartments
        fields = ['name', 'description', 'location', 'image',]


class HouseAddForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'
        exclude = ['paid', 'booked']




class AllocateRoomForm(forms.ModelForm):
    
    class Meta:
        fields = ['tenant','room', 'paid', 'approved', 'allocate_date']
        model = AllocateRoom
        widgets = {
                'allocate_date': forms.DateInput(),
                
            }