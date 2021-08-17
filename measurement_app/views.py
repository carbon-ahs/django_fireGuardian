import math
from django.shortcuts import render, redirect
from django.http import Http404
from math import ceil

from .models import officeDetail
'''
from .models import 
from .forms import 
'''
app_name = 'Fire Guardian'

def home(request):
    contex = {
        'key': 'value',
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
    try:
        all_office = officeDetail.objects.all()
    except officeDetail.DoesNotExist:
        raise Http404("No Model, Pls check migration.") 

    last_office = all_office.reverse()[0]
    sz = last_office.office_size
    if last_office.office_type == 'in':
        required_extenguiter = math.ceil(sz/1000) 
    elif last_office.office_type == 'cm':
        required_extenguiter = math.ceil(sz/3000) 
    elif last_office.office_type == 'rs':
        required_extenguiter = math.ceil(sz/5000) 
     
    contex = {
        'last_office': last_office,
        'header' : header,
        'key': 'value',
        'app_name' : app_name,
        'sz': sz,
        'required_extenguiter': required_extenguiter,
    }
    return render(request, 'last_entry.html', contex)
