from django.db import models
from  houses.models import Rooms
from users.models import UserProfile
from datetime import datetime
import random
import string

MONTHS_SELECT = [
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
]
PAYMENT_STATUS_CHOICES = [
    ('approved', 'Approved'),
    
    ('pending', 'Pending'),
]


class Year(models.Model):
    name = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return f'{self.name}'

class RentDetails(models.Model):
    STATUS_CHOICES = [
        ('refunded', 'Refunded'),
        ('open', 'open'),
        ('closed', 'closed'),
    ]
    # tenant = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    year = models.ForeignKey(Year, on_delete=models.DO_NOTHING, null=True)
    pay_for_month = models.CharField(max_length=20, choices=MONTHS_SELECT)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='open',null=True)
    start_date = models.DateTimeField(null=True)
    due_date = models.DateTimeField(null=True) 

    def __str__(self):
        return f"Rents For {self.pay_for_month}, {self.year} "

    class Meta:
        verbose_name_plural = 'Rent Details'
        unique_together = ('year', 'pay_for_month')


class RentPayments(models.Model):
    rent_details = models.ForeignKey(RentDetails, on_delete=models.CASCADE, null=True)
    tenant = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True, blank=True)    
    amount = models.IntegerField(null=True, blank=True)
    paid_on = models.DateField(auto_created=True, null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    added_on = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     room = self.room
    #     self.amount = self.room.price
    #     self.room.paid = True
    #     self.room.booked = True
    #     self.rent_details.cleared = True
    #     room.save()
        
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Handset rent payment for {self.room} rent paid by {self.tenant}"

    class Meta:
        verbose_name_plural = "Rent Payments"


class MpesaOnlinePayments(models.Model):
        STATUS_OPTIONS = [
            ('pending','Pending'),
            ('approved', 'Approved'),
        ]
        tenant = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True,)
        RentDetails = models.ForeignKey(RentDetails, on_delete=models.CASCADE, related_name='payment')
        Room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True, blank=True)    
        MerchantRequestID = models.CharField(max_length=155,null=True, blank=True)
        CheckoutRequestID = models.CharField(max_length=155, null=True, blank=True)
        Amount = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
        MpesaReceiptNumber = models.CharField(max_length=100, null=True, blank=True)
        TransactionDate = models.CharField(max_length=55, null=True, blank=True)    
        PhoneNumber = models.CharField(max_length=25, null=True, blank=True)
        ResultCode = models.CharField(max_length=100, null=True, blank=True)
        ResultDesc = models.CharField(max_length=100, null=True, blank=True)
        Approved = models.BooleanField(default=False)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)

        # def save(self, *args,  **kwargs):
            
        #     rent_details = RentDetails.objects.filter(cleared = False)
        #     if self.Approved == True:
        #         selrent_details.cleared = True
        #     else:
        #         rent_details.cleared = False
        #     return super().save(*args, **kwargs) 

        def __str__(self):
            return f"Online rents payments for {self.Room} {self.RentDetails.pay_for_month} {self.RentDetails.year} paid by {self.tenant}"

        class Meta:
            unique_together = ('tenant', 'RentDetails')
            verbose_name = "Mpesa Online Payments"
            verbose_name_plural = verbose_name
            
class TenantRentPayments(models.Model):
    rent_details = models.ForeignKey(RentDetails, on_delete=models.CASCADE, null=True)
    tenant = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True, blank=True)    
    amount = models.IntegerField(null=True, blank=True)
    MerchantRequestID = models.CharField(max_length=100, null=True)   
    CheckoutRequestID = models.CharField(max_length=100, null=True)   
    paid_on = models.DateField(auto_now_add=True, null=True, blank=True)   
    confirmed = models.BooleanField(default=False)
    added_on = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return f' {self.rent_details} paid by {self.tenant} on {self.paid_on}'    
    class Meta:
            unique_together = ('rent_details','tenant')
            verbose_name = "Tenant Rent Payments"
            verbose_name_plural = verbose_name
            