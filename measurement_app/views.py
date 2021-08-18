import math
from django.contrib import messages
from measurement_app.forms import officeDetailForm
from django.shortcuts import render, redirect
from django.http import Http404
from math import ceil

from .models import officeDetail
'''
from .models import 
from .forms import 
'''
app_name = 'Fire Guardian'

def prototype_output(office):
    sz = office.office_size

    if office.office_type == 'in':
        type = 'Industrial'
        required_extenguiter = math.ceil(sz/1000) - office.present_fire_extinguisher_number 
    elif office.office_type == 'cm':
        type = 'Commercial'
        required_extenguiter = math.ceil(sz/3000) - office.present_fire_extinguisher_number 
    elif office.office_type == 'rs':
        type = 'Residential'
        required_extenguiter = math.ceil(sz/5000) - office.present_fire_extinguisher_number
 
    op = f'Hlw! wellcome! Your are currently in a {type} building. your space is {sz} sqft. You need { required_extenguiter } Fire Extenguiser'
    if required_extenguiter <= 0:
        op = f'Hlw! wellcome! Your are currently in a {type} building. your space is {sz} sqft. Acording to Bangladesh low, you have enough equpments'
    return op

def home(request):
    form = officeDetailForm()
    contex = {
        'key': 'value',
        'form': form,
    }
    return render(request, 'home.html', contex)



def about(request):
    contex = {
        'key': 'value',
    }
    return render(request, 'about.html', contex)

def tempu(request):
    header = 'TEMPU VRUMMMM'

    contex = {
        'header' : header,
        'key': 'value',
        'app_name' : app_name,
    }
    return render(request, 'tempu.html', contex)

def all_office(request):
    header = 'All Office'

    

    contex = {
        'header' : header,
        'key': 'value',
        'app_name' : app_name,
    }
    return render(request, 'tempu.html', contex)


def last_entry_view(request):
    header = 'Last Entry'
    if request.method == 'POST':
        form = officeDetailForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully!!')
        else:
            messages.success(request, 'eror !!')

        redirect(last_entry_view)
   
    try:
        all_office = officeDetail.objects.all()
    except officeDetail.DoesNotExist:
        raise Http404("No Model, Pls check migration.") 
    
    last_office = all_office[len(all_office)-1]

    op = prototype_output(last_office)
     
    contex = {
        'last_office': last_office,
        'header' : header,
        'key': 'value',
        'app_name' : app_name,
        'op': op,
        #'sz': sz,
        #'required_extenguiter': required_extenguiter,
    }
    return render(request, 'last_entry.html', contex)
