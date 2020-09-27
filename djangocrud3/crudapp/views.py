# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def load_form(request):
    form = EmployeeForm()
    return render(request,'add.html',{'form':form})

def add(request):
    form = EmployeeForm(request.POST)
    if form.is_valid():
        form.save()
    	return redirect('/show')

@csrf_exempt
def addmodal(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		contact = request.POST.get('contact')
		Employee.objects.create(
		ename = name,
		email = email,
		econtact = contact,
		)

		response_data = {}
		response_data['name'] = name
		response_data['email'] = email
		response_data['contact'] = contact
		#return HttpResponse("Createde")
		#employee = serializers.serialize('json',Employee.objects.all())-Wrong method
		#employee = list(Employee.objects.values('ename','email','econtact'))-Right
		employee = list(Employee.objects.values_list('id','ename','email','econtact'))
		#employee = Employee.objects.all()-Wrong method
		#employee = list(Employee.objects.all())
		return JsonResponse({'employee':employee})

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

