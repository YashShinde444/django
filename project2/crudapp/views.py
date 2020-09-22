# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
import datetime
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# Create your views here.
def show(request):
    employee = Employee.objects.all()
    employeeList = []
    for emp in employee:
        data = {"id":emp.eid,"name":emp.ename,"email":emp.email,"contact":emp.econtact}
        employeeList.append(data)
    print(employeeList)
    return HttpResponse(json.dumps({"response_code":200,"Status":"Success","EmployeeList":employeeList}),content_type="application/json")

#hyat ahe na upate functionality barobar ahe ki ata postman madhe kasa karaycha sanga
@api_view(['POST'])
def create(request):
	try:
		data = request.data
		print(data) 
		try:
			employee = Employee.objects.get(eid=data["eid"])
		except:
			employee = Employee()
		employee.eid = data['eid']
		employee.ename = data['ename']
		employee.email = data['email']
		employee.econtact = data['econtact']
		employee.save()
		return HttpResponse(json.dumps({"response_code":200,"Status":"Success"}),content_type="application/json")
	except Exception as e:
		error=str(e)
        return HttpResponse(json.dumps({"status":"fail","response_code":500,"error":error}),content_type="application/json")


def hello_world_view(request):
	return HttpResponse('<h1>Hello This is response from django appliocati0on</h1>')

def date_time_view(request):
	date=datetime.datetime.now()
	s='<h1>THe current date time is:'+str(date)+'</h1>'
	return HttpResponse(s)

def good_morning_view(request):
	return HttpResponse('<h1>Hello Friend</h1>')

def welcome(request):
	return render(request, "Welcome.html")

def load_form(request):
	form = EmployeeForm
	return render(request,"index.html",{'form':form})

def add(request):
	form = EmployeeForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect('/show')

def edit(request,id):
	employee = Employee.objects.get(id=id)
	return render(request, 'edit.html',{'employee':employee})

def update(request,id):
	employee = Employee.objects.get(id=id)
	form = EmployeeForm(request.POST, instance=employee)
	if form.is_valid():
		form.save()
	return redirect('/show')

def delete(request,id):
	employee = Employee.objects.get(id=id)
	employee.delete()
	return redirect('/show')

