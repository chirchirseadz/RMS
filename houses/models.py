from django.db import models
# from django.contrib.auth.models import User


from django.urls import reverse

# Create your models here.


class Apartments(models.Model):
    name = models.CharField(max_length=100, db_index=True, null=True)
    description = models.TextField(blank=False, null=True)
    location = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)
    
    def __str__(self):
        return self.name

    def get_absolute_urls(self):
        return reverse(args=[self.id])

    class Meta:
        verbose_name_plural = 'Apartments'

class Category(models.Model):
    
    name = models.CharField(max_length=100, db_index=True, null=True)
    
    
    def __str__(self):
        return self.name

    def get_absolute_urls(self):
        return reverse('house_type', args=[self.id])

    class Meta:
        verbose_name_plural = 'Categories'




class Rooms(models.Model):
   
    FLOORS  = (
        ('Ground Floor', 'Ground Floor'),
        ('First Floor', 'First Floor'),
        ('Second Floor', 'Second Floor'),
        ('Third Floor', 'Third Floor'),
        ('Fourth Floor', 'Fourth Floor'),
        ('Fifth Floor', 'Fifth Floor'),
        ('sixth Floor', 'sixth Floor'),
        ('Eighth Floor', 'Eighth Floor'),
        ('Nineth Floor', 'Nineth Floor'),
        ('Tenth Floor', 'Tenth Floor'),
    )
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
        
    ]
    MAINTAINANCE = [
        ('Under Maintainance', 'Under Maintainance'),
        ('In Good Condition', 'In Good Condition'),
        
    ]
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE, null=True)
    house_number = models.PositiveBigIntegerField(null=True, verbose_name = 'Room Number')
    floor = models.CharField(max_length=50, choices=FLOORS, null=True)
    house_type = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Room Category')
    price = models.IntegerField()
    house_description = models.TextField(blank=True, null=True, verbose_name='Room Description')
   
    image1 = models.ImageField(default='empty.jpg')
    image2 = models.ImageField(default='empty.jpg')
    image3 = models.ImageField(default='empty.jpg')
    add_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='Ready To Move In')
    maintainance = models.CharField(max_length=20, choices=MAINTAINANCE,default='In Good Condition')
    booked = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    class Meta: 
        unique_together = ('room', 'apartment')

    def __str__(self):
        return f'[--Room [{self.house_number}] {self.apartment}---] '
    
    class Meta:
        verbose_name_plural = 'Houses'
        unique_together = ('apartment', 'house_number')


class Navigation(models.Model):
    title = models.CharField(max_length=50,null=True, blank=True)
    logo = models.ImageField(null=True)

    class Meta:
        verbose_name_plural = 'Header'

    def __str__(self):
        return self.title


class Slider(models.Model):
    
    slide_title = models.CharField(max_length=55, null=True)
    house_type = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    rent = models.PositiveBigIntegerField(null=True)
    location = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.slide_title



    class Meta:
        verbose_name_plural = 'Slider'


#  These are the orgamization contacts
class Contacts(models.Model):
    name = models.CharField(max_length=40, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)
    contact_info = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=15, null=True)
    location = models.CharField(max_length=15, null=True , blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contacts'


