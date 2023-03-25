from django.db import models
from houses.models import Apartments, Rooms
from django.contrib.auth.models import User, AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class CustomUser(AbstractUser):
     is_admin = models.BooleanField(default=False)
     is_tenant = models.BooleanField(default=False)
     policy_agreement = models.BooleanField(default=False, null=True)

class UserProfile(models.Model):
    name = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=13, null=True)
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True, verbose_name='Rented Room', blank=True)
    address = models.CharField(max_length=50, null=True)
    profile_pic = models.ImageField(default='empty.jpg', null=True)
    created = models.DateTimeField(auto_now=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta: 
        unique_together = ('room',)

    def save(self, *args, **kwargs):
        # call the parent save() method to save the instance first
        super(UserProfile, self).save(*args, **kwargs)

        # check if a room is assigned to the user profile
        if self.room:
            # assign the room to the user profile
            room = self.room
            room.tenant = self
            room.status = 'Not Available'
            room.paid = True
            room.booked = True
            room.save()

    def __str__(self):
        return f'{self.name}'
    