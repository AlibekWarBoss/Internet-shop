from django.shortcuts import render
from .models import *


def index (request):
    sp_list = Smartphone.objects.all()
    camera_list = Camera.objects.all()
    laptop_list = Laptop.objects.all()
    earphone_list = Earphone.objects.all()
    context = {'sp_list' : sp_list, 'camera_list' : camera_list,
    'laptop_list' : laptop_list, 'earphone_list' : earphone_list}
    return render(request,'mainApp/index.html',context)

def smartphone(request):
    sp_list = Smartphone.objects.all()
    context = {'sp_list':sp_list}
    return render(request, 'mainApp/some/smartphone.html', context)

def camera(request):
    camera_list = Camera.objects.all()
    context = {'camera_list':camera_list}
    return render(request, 'mainApp/some/cameras.html', context)

def laptop(request):
    laptop_list = Laptop.objects.all()
    context = {'laptop_list':laptop_list}
    return render(request, 'mainApp/some/laptop.html', context)

def earphone(request):
    earphone_list = Earphone.objects.all()
    context = {'earphone_list':earphone_list}
    return render(request, 'mainApp/some/earphones.html', context)


    ##details##
def camera_detail(request, camera_name):
    camera_detail = Camera.objects.get(name = camera_name)
    template = 'mainApp/some/camera_detail.html'
    context = {'camera_detail' : camera_detail}
    return render(request,template,context)



def smartphone_detail(request, smartphone_name):
    smartphone_detail = Smartphone.objects.get(name = smartphone_name)
    template = 'mainApp/some/smartphone_detail.html'
    context = {'smartphone_detail' : smartphone_detail}
    return render(request,template,context)


def earphone_detail(request, earphone_name):
    earphone_detail = Earphone.objects.get(name = earphone_name)
    template = 'mainApp/some/earphone_detail.html'
    context = {'earphone_detail' : earphone_detail}
    return render(request,template,context)

# def laptop_detail(request, laptop_name):
#     laptop_detail = Laptop.objects.get(name = laptop_name)
#     template = 'mainApp/some/laptop_detail.html'
#     context = {'laptop_detail' : laptop_detail}
#     return render(request,template,context)
