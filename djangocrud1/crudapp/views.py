# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.http import HttpResponse
# Create your views here.

def load_form(request):
    form = EmployeeForm()
    print form
    return render(request,'add.html',{'form':form})

def add(request):
    form = EmployeeForm(request.POST)
    if form.is_valid():
        form.save()
    #return HttpResponse("Added")
    #return redirect('/load_form')
    return redirect('/show')

def show(request):
    employee = Employee.objects.all()
    return render(request,'show.html',{'employee':employee})

def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})

def update(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')