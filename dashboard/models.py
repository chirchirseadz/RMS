from django.db import models
from houses.models import *
from users.models import *
from django.db import transaction

# Create your models here.
class MessagesFromTenants(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(blank=True, null=True)
    message_date = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.subject
        
    class Meta:
        verbose_name_plural = 'Messages From Tenants'


class NoticesToTenants(models.Model):  
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(blank=True, null=True)
    notice_date = models.DateTimeField(auto_created=True)
    message_date = models.DateField(auto_created=True,null=True)
    
    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = 'NoticesToTenants'





class Complaints(models.Model):
    STATUS_CHOICES = (
        ('Received', 'Received'),
        ('Processing', 'Processing'),
        ('Resolved', 'Resolved'),
        ('Dropped', 'Dropped'),
    )
    PRIORITY = (
        ('High Priority', 'High Priority'),
        ('Medium Priority', 'Medium Priority'),
        ('Less Priority', 'Less Priority'),
        
    )
    reported_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True,verbose_name='your Username')
    priority = models.CharField(max_length=100, choices=PRIORITY, null=True)
    subject = models.CharField(max_length=100, blank=True, help_text="other type of isses...", null=True)
    status = models.CharField(max_length=20,  choices=STATUS_CHOICES, null=True)
    description = models.TextField(verbose_name="Describe the situation", null=True)
    created = models.DateTimeField(auto_created=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"reported by {self.reported_by}"

    class Meta:
        verbose_name_plural = 'Complaints'

class RoomBooking(models.Model):

    CHOICES = (
        ('Pending', 'Pending'),
        ('Already Sorted', 'Already Sorted'),
    )
    requested_by = models.CharField(max_length=40, null=True, verbose_name='Your Name')
    room_booked = models.ForeignKey(Rooms, on_delete=models.CASCADE,null=True)
    email = models.EmailField(null=True, verbose_name='Your Email Address')
    phone_number = models.CharField(max_length=13, null=True, verbose_name='Active Phone Number.')
    request_info = models.TextField(max_length=100, blank=True, help_text="Your Request Information", null=True)
    status =  models.CharField(max_length=100, null=True, choices=CHOICES, default='Pending')
    date_requested = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Room Requested By {self.requested_by}'
    


class AllocateRoom(models.Model):
    PAID = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    tenant = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, null=True)
    room = models.OneToOneField(Rooms, on_delete=models.CASCADE,null=True, unique=True)
    paid = models.CharField(max_length=10, choices=PAID, null=True)
    approved = models.BooleanField(default=False, null=True)
    allocate_date = models.DateField(auto_created=True, null=True)

    
    class Meta:
        unique_together = ('tenant','room')
    def __str__(self):
        return f'Alocated {self.room} to {self.tenant}'

    def save(self, *args, **kwargs):
        with transaction.atomic():

            # Get the room object
            room = self.room            
            # Set the room's status to "Not Available"
            room.status = "Not Available"
            room.paid = True
            room.save()
            tenant = self.tenant
            tenant.room = room
            tenant.apartment = room.apartment
            tenant.save()


            super().save(*args, **kwargs)