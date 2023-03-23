from django.shortcuts import render, get_object_or_404, redirect
from . models import Rooms,Category, Navigation, Slider, Contacts
from django.core.paginator import Paginator, EmptyPage
from . filters import Housefilter
from django.contrib import messages
from dashboard.forms import MessagesFromTenantsForm
from .forms import RoomBookingForm
from django.core.mail import BadHeaderError, send_mail

from core.settings import EMAIL_HOST_USER
# from django.http.response import JsonResponse

# Create your views here.

def index(request):
    houses = Rooms.objects.all() 
    myFilter = Housefilter(request.GET, queryset=houses)
    houses = myFilter.qs   
    context = {
        'houses': houses,
        
    }
    return render(request, 'front/index.html', context)


def about(request):
    return render(request, 'front/about.html')


def houses(request):
    houses = Rooms.objects.all()

    paginator = Paginator(houses, 4)
    page_num = request.GET.get('page', 1)

    try:
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(1)

    myFilter = Housefilter(request.GET, queryset=houses)
    houses = myFilter.qs

    context = {
        'houses': houses,
        'page': page,
        'page_num': page_num,
        'myFilter': myFilter,
    }


    return render(request, 'front/houses.html',context)


def category_list(request, pk):
    # category = get_object_or_404(,id=pk)
    category = Category.objects.get(id=pk)
    houses = Rooms.objects.filter(house_type=category)
    house_count = Rooms.objects.filter(house_type=category).count()

    context = {
        'category': category,
        'houses': houses,
        'house_count':house_count,
    }
    return render(request, 'front/house_type.html', context)

def available_houses(request):
    houses = Rooms.objects.all()
    house_count = Rooms.objects.filter(booked=False, paid=False).count()
    myFilter = Housefilter(request.GET, queryset=houses)
    houses = myFilter.qs

    context = {
        'houses': houses,
        'myFilter': myFilter,
        'house_count':house_count,
    }
    return render(request, 'front/available_houses.html', context)

#  This is the view where all bookinns are made 

def house_details(request,id):
    house_obj = Rooms.objects.get(id=id)
    # user = CustomUser.object.get(id=id)
    # house.booked = False
    if request.method == 'POST':
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.room_booked = house_obj
            data.save()
            form.save()
            
            email = form.cleaned_data.get('email')
            send_mail(
                'ROOM BOOKING REQUEST ', # subject 
                'There is an anonymous user who wants to book a Room. visit the system For more information !!',
                 email,   # from
                 ['sydneychirchir@gmail.com'],
            )
            data.save()
            form.save()
            messages.success(request, 'Your Request Submited Successfully !! ')
            return redirect('available_houses')
        else:
            messages.error(request, 'Your Request Not Submited Check your input !! ')
    #  payment logics and fuctions 

    # house.booked = True
    else: 
        form = RoomBookingForm()
    context = {
        'house':house_obj,
        'form': form
    }
    return render(request, 'front/house_detail.html', context)



def contact_page(request):
    contact_info = Contacts.objects.all()
    if request.method == 'POST':
        # message_sent = False
        message_form = MessagesFromTenantsForm(request.POST)
        try:
            if message_form.is_valid():
                your_name = message_form.cleaned_data.get('your_name')
                email = message_form.cleaned_data.get('email')
                subject = message_form.cleaned_data.get('subject')
                message = message_form.cleaned_data.get('message')
                message_form.save()

                send_mail(
                    subject,  # subject 
                    message,  # message   
                    email, # from 
                    ['EMAIL_HOST_USER'], # To email 
                    # "This is the message from  chisquare-connections  contact us page ", 
                    fail_silently = False
                    
                )

                # message_sent = True

                messages.success(request, 'Your message was sent successfully !')

                return redirect('contact')
            

        except:
           messages.warning(request, 'You are currently offline !!! ' )
           return redirect('contact')
            # return HttpResponse('<script> window.alert("Thanks for your comment")</script>')
    else:
        message_form = MessagesFromTenantsForm()
        your_name = MessagesFromTenantsForm()
    context = {
        'message_form': message_form,
        'your_name':your_name
    }

    return render(request, 'front/contact.html', context)

# ######%%%%%%%%%%%%%%%%%^^^^^^^#######################%%%^^^^^^^&&^^%%%%%%%%%%%%%%%%%%%%%%%%%%%

#  CONTEXT PREPROCESSOR INFORMATIONS 

def categories(request):
    return  {
        'categories': Category.objects.all()
    }

def nav_info(request):
    return {
        'nav_info': Navigation.objects.all()
    }

def slider_info(request):
    return {
        'slider_info': Slider.objects.all()
    }

def nav_info(request):
    return {
        'nav_info' : Navigation.objects.all()
    }



