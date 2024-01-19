from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

def base(request):

    return render(request,'base.html')

def adm_dept(request):

    return render(request,'admin_department.html')


 
 
# Create your views here.
