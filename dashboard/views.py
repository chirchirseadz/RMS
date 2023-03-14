from django.shortcuts import render, redirect
from users.models import UserProfile, CustomUser
from django.contrib.auth.models import User
from .models import RoomBooking, Complaints, NoticesToTenants
from houses.models import Apartments, Category,Rooms, Navigation, Slider, Contacts
from houses.forms import RoomBookingForm
from . forms import ActivateUserForm, ApartmentAddForm, HouseAddForm, ManageTenantForm, AdminComplaintsForm, NoticesToTenantsForm, ComplaintsForm, SliderForm, ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.db import transaction
from houses.forms import AdminBookingUpdateForm
from . utils import resize_image

# Create your views here.
@login_required(login_url='login')
def index(request):
    tenants = CustomUser.objects.filter(is_admin=False)
    number_of_tenants = tenants.count()

    category = Category.objects.all()
    number_of_category = category.count()

    apartments = Apartments.objects.all()
    number_of_apartments = apartments.count()

    houses = Rooms.objects.all()
    number_of_houses = houses.count()

    house_requests = RoomBooking.objects.all().order_by('-date_requested')
    notices = NoticesToTenants.objects.all()

    context = {
        'notices': notices,
        
        'tenants': tenants,
        'number_of_tenants': number_of_tenants,

        'category': category,
        'number_of_category': number_of_category,

        'apartments': apartments,
        'number_of_apartments': number_of_apartments,

        'houses': houses,
        'number_of_houses': number_of_houses,

        'house_requests' :house_requests,
    }
    return render(request, 'dashboard/index.html', context)


def adminbookingupdate(request, id):
    room_obj = RoomBooking.objects.get(id=id)
    
    if request.method == 'POST':
        form = AdminBookingUpdateForm(request.POST, instance=room_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have Updated the Booking info Successfully !')
            return redirect('index_page')
    else:

        form = AdminBookingUpdateForm(instance=room_obj)

    context = {
        'form' : form 
    }
    return render(request, 'dashboard/partials/booking_update.html', context)


@login_required(login_url='login')
def list_of_tenants(request):
    tenants = CustomUser.objects.filter(is_admin=False)
    tenants_obj = CustomUser.objects.filter(is_active=False)
    number_of_inactive_tenants = tenants_obj.count()
    number_of_tenants = tenants_obj.count()
    context = {
        'number_of_tenants': number_of_tenants,
        'tenants': tenants,
        'number_of_inactive_tenants': number_of_inactive_tenants,
    }
    return render(request, 'dashboard/partials/list_of_tenants.html', context )

@login_required(login_url='login')
def list_of_in_active_tenants(request):
    tenants = CustomUser.objects.filter(is_active=False)
    tenant_obj = CustomUser.objects.filter(is_admin=False)
    number_of_inactive_tenants = tenants.count()
    number_of_tenants = tenant_obj.count()
    context = {
        'number_of_tenants': number_of_tenants,
        'tenants': tenants,
        'number_of_inactive_tenants':number_of_inactive_tenants
    }
    return render(request, 'dashboard/partials/list_of_inactive_tenants.html', context )

@login_required(login_url='login')
def single_tenant_view(request, id):
    tenant = CustomUser.objects.get(id=id)
        
    context = {
        'tenant': tenant,
    }
    return render(request, 'dashboard/partials/single_tenant.html', context)

@login_required(login_url='login')
def ManageTenant(request, id):
    user = CustomUser.objects.get(id=id)
    tenant = UserProfile.objects.get(id=id)
    if request.method == 'POST':
        tenant_form = ManageTenantForm(request.POST, request.FILES, instance=tenant)
        user_form = ActivateUserForm(request.POST, instance=user)
        if tenant_form.is_valid() and user_form.is_valid():
            tenant_form.save()
            user_form.save()
            messages.success(request, 'Tenant Details Updated Successfully !!! ')
            return redirect("index_page")
        else:
            messages.warning(request, 'Tenant Details Not Updated Successfully !!!' )
    else:
        user_form = ActivateUserForm(instance=user)
        tenant_form = ManageTenantForm(instance=tenant)
        tenant = ""
        # tenant_form = ActivateUserForm(instance=request.user)

    context = {
        'tenant_form': tenant_form,
        'user_form':user_form, 
        'tenant': tenant,
    }
    return render(request, 'dashboard/partials/edit_tenant.html', context)
    

# APARTMENTS 

# add apartment
@login_required(login_url='login') 
def AddApartment(request):
    if request.method == 'POST':
        form = ApartmentAddForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            image = resize_image(image, 500, 600)
            data = form.save(commit=False)
            data.image = image  
            data.save()
            messages.success(request, 'Apartment Added Successfully !! ')
            return redirect("index_page")
        else:
            messages.error(request, 'Apartment Not Added. Check Your Input !! ')
    else:
        form = ApartmentAddForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/partials/add_apartment.html', context)
    
@login_required(login_url='login')
def ApartmentsView(request):
    apartment = Apartments.objects.all()
    number_of_appartments = apartment.count()
    context = {
        "apartment": apartment,
        'number_of_appartments': number_of_appartments
    }
    return render(request, 'dashboard/partials/apartments.html',context)

@login_required(login_url='login')
def ApartmentUpdate(request, id):
    apartment_obj = Apartments.objects.get(id=id)
    if request.method == 'POST':
        update_form = ApartmentAddForm(request.POST, instance=apartment_obj)
        if update_form.is_valid():
            image = update_form.cleaned_data.get('image')
            image = resize_image(image, 500, 600)
            data = update_form.save(commit=False)
            data.image = image  
            data.save()
            messages.success(request, 'Apartment Updated Sucessfully !!')
            return redirect('index_page')
        else:
            messages.error(request, "Apartment did'nt Updated !!!!" )
    else:
        update_form = ApartmentAddForm(instance=apartment_obj)
        apartment_obj = ''
    context = {
        'update_form': update_form
    }
    return render(request, 'dashboard/partials/apartments_update.html',context)

@login_required(login_url='login')
def DeleteApartment(request, id):
    apartments = Apartments.objects.get(id=id)
    apartments.delete()
    messages.success(request, 'Apartment deleted successfully')
    
    return redirect('index_page')

# ROOMS ADMIN FUNCTIONALITIES
@login_required(login_url='login')
def AddHouse(request):
    if request.method == 'POST':
        add_form = HouseAddForm(request.POST, request.FILES)
        if add_form.is_valid():
            image1 = add_form.cleaned_data.get('image1')
            image1 = resize_image(image1, 500, 600)
            image2 = add_form.cleaned_data.get('image2')
            image2 = resize_image(image2, 500, 600)
            image3 = add_form.cleaned_data.get('image3')
            image3 = resize_image(image3, 500, 600)
            data = add_form.save(commit=False)
            data.image1 = image1
            data.image2 = image2
            data.image3 = image3
            data.save()
            messages.success(request, 'House Added succesfully !! ')
            return redirect("index_page")
    else:
        add_form = HouseAddForm()

    context = {
        'add_form': add_form
    }
    return render(request, 'dashboard/partials/house_add.html', context)

@login_required(login_url='login')
def HousesView(request):
    houses = Rooms.objects.all()
    number_of_houses = houses.count()
    context  = {
        "houses": houses,
        'number_of_houses': number_of_houses
    }
    return render(request, 'dashboard/partials/houses.html', context) 

@login_required(login_url='login')
def HouseUpdate(request, id):
    obj = Rooms.objects.get(id=id)
    if request.method == 'POST':
        form = HouseAddForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            image1 = form.cleaned_data.get('image1')
            image1 = resize_image(image1, 500, 600)
            image2 = form.cleaned_data.get('image2')
            image2 = resize_image(image2, 500, 600)
            image3 = form.cleaned_data.get('image3')
            image3 = resize_image(image3, 500, 600)
            data = form.save(commit=False)
            data.image1 = image1
            data.image2 = image2
            data.image3 = image3
            data.save()
            messages.success(request, 'House Added succesfully !! ')
            return redirect("index_page")
    else:
        form = HouseAddForm(instance=obj)
        
    context = {
        'form': form
    }

    return render(request, 'dashboard/partials/house_update.html', context)


@login_required(login_url='login')
def DelRoom(request,id):
    room = Rooms.objects.get(id=id)
    room.delete()
    messages.success(request, 'Room deleted Successfully !!')
    return redirect('index_page')



# NOTICES FUNCTIONALITIES

@login_required(login_url='login')
def TenantComplaints(request):
    complaints = Complaints.objects.all().order_by('-created')
    context = {
        'complaints': complaints,
    }
    return render(request, 'dashboard/partials/complaints.html', context)

def TenantComplaintsUpdate(request, id):
    complaints = Complaints.objects.get(id=id)
    if request.method == 'POST':
        form = AdminComplaintsForm(request.POST, instance=complaints)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comlaint Updated successfully !! ' )
            return redirect("index_page")
    else:
        form = AdminComplaintsForm(instance=complaints)
    context = {
        'form': form
    }
    return render(request, 'dashboard/partials/complaints_update.html', context)


@login_required(login_url='login')
def MessagesToTenants(request):
    if request.method == 'POST':
        form = NoticesToTenantsForm(request.POST)
        if form.is_valid():
            users = CustomUser.objects.all()
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            for user in users:
                send_mail(
                    subject, # subject 
                    message,
                    ['info@chi-squareconnections.com',], # from
                    [user.email],
                    # fail_silently=True
                )
            form.save()
            messages.success(request, 'Message sent SuccessFully !! ' )
            return redirect('index_page')
    else:
        form = NoticesToTenantsForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/partials/admin_message.html', context)


#  File complaints 
@login_required(login_url='login')
def FileComplaint(request):
    if request.method == 'POST':
        form = ComplaintsForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.reported_by = request.user
            
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('description')
            try:
                send_mail(
                    subject,
                    message,
                    request.user.email,
                    ['info@chi-squareconnections.com',],
                    fail_silently=False,
                    )
            except:
                messages.warning(request, "Your Complaint did'nt submit. Your email is invalid !!! ")
            info.save()
            messages.success(request, 'Complaint sent Successfully !! ')
            return redirect('index_page')
    else:
        form = ComplaintsForm()
    context = {
        'form': form 

    }
    return render(request, 'dashboard/partials/make_complaint.html', context)


#  Create Slider
def createslider(request):
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slider Created successfully !! ')
            return redirect('index_page')
    else:
        form = SliderForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/partials/slider.html', context)

# VIEW SLIDER

def viewsliders(request):
    slider = Slider.objects.all()
    number_of_slides = slider.count()
    context = {
        'slider': slider,
        'number_of_slides': number_of_slides
    }
    return render(request, 'partials/sliders.html', context)


def updateslider(request, id):
    slider = Slider.objects.get(id=id)
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES, instance=slider)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slider Updated successfully !! ')
            return redirect('index_page')
    else:
        form = SliderForm(instance=slider)
    context = {
        'form': form
    }
    return render(request, 'dashboard/partials/slider_update.html', context)
    

# DELETE SLIDER

def deleteslider(request, id):
    slider = Slider.objects.get(id=id)
    slider.delete()


def create_contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contacts Created successfully !!! ')
            return redirect('index_page')
        else:
            messages.error(request, 'Contacts not created. Check Your inputs')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/partials/contact_create.html', context)


def view_contacts(request):
    contacts = Contacts.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'dashboard/partials/contactlist.html', context)


def delete_contacts(request,id):
    contact = Contacts.objects.get(id=id)
    contact.delete()

    messages.success(request, 'Contact Deleted Successfully !!')
    return redirect('index_page')


def contacts(request):
    return {
        'contacts': Contacts.objects.all()
    }

# def MessagesToTenantsUpdate(request, id):
#     return render(request, 'dashboard/partials/complaints_update.html', context)


# @login_required(login_url='login')
# def MessageFromTenants(request):
#     return render(request, 'dashboard/partials/complaints.html', context)

# def MessagesFromTenantsUpdate(request, id):
#     return render(request, 'dashboard/partials/complaints_update.html', context)






