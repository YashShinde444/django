# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.http import HttpResponse
# Create your views here.

def load_form(request):
	form = EmployeeForm
	return render(request,'index.html',{'form':form})

def add(request):
	form = EmployeeForm(request.POST)
	if form.is_valid():
		form.save()
		return redirect('/show')

def show(request):
	employee=Employee.objects.all
	return render(request,'show.html',{'employee':employee})

