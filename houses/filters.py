import django_filters
from django import forms

from .models import *


class Housefilter(django_filters.FilterSet):
    
    class Meta:
        model = Rooms
        fields = ['house_type','floor','price',]
        # fields = "__all__"

       

