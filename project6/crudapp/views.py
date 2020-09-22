# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.http import HttpResponse

# Create your views here.

def load_form(request):
	form = EmployeeForm
	return render(request,"index.html",{'form':form})

def add(request):
    form = EmployeeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/show')

def show(request):
    employee = Employee.objects.all
    return render(request,'show.html',{'employee':employee})

def edit(request,id):
	employee = Employee.objects.get(id=id)
	return render(request, 'edit.html',{'employee':employee})

def update(request,id):
    employee=Employee.objects.get(id=id)
    #print{employee}
    form=EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    #return HttpResponse(form)


def delete(request,id):
	employee = Employee.objects.get(id=id)
	employee.delete()
	return redirect('/show')