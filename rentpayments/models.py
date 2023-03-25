from django.db import models
from  houses.models import Rooms
from users.models import UserProfile

import random
import string

class Year(models.Model):
    name = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return f'{self.name}'

class RentPayments(models.Model):
    MONTH_CHOICES = (
        ('JAN', 'January'),
        ('FEB', 'February'),
        ('MAR', 'March'),
        ('APR', 'April'),
        ('MAY', 'May'),
        ('JUN', 'June'),
        ('JUL', 'July'),
        ('AUG', 'August'),
        ('SEP', 'September'),
        ('OCT', 'October'),
        ('NOV', 'November'),
        ('DEC', 'December'),
    )

    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        
    ]
    tenant = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE,null=True)
    year =  models.ForeignKey(Year, on_delete=models.CASCADE,null=True)
    month = models.CharField(max_length=3, choices=MONTH_CHOICES,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    amount = models.IntegerField(null=True)
    account_reference = models.CharField(max_length=50,null=True)
    transaction_desc = models.CharField(max_length=255,null=True)
    callback_url = models.URLField(max_length=255,null=True)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, null=True)
    transaction_id = models.CharField(max_length=50, blank=True,null=True)
    error_message = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f'{self.tenant.name} - {self.month} - {self.amount}'

   

    