# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
import datetime
from django.shortcuts import render, redirect
from .forms import UsersForm
from .models import Users

# Create your views here.

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
	form = UsersForm
	return render(request,"index.html",{'form':form})

def add(request):
	form = UsersForm(request.POST)
	if form.is_valid():
		form.save
		return redirect('/show')

def show(request):
	users = Users.objects.all
	return render(request, 'show.html',{'Users':Users})

def edit(request,id):
	users = Users.objects.get(id=id)
	return render(request, 'edit.html',{'Users':Users})

def update(request,id):
	users = Users.objects.get(id=id)
	form = UsersForm(request.POST, instance=Users)
	if form.is_valid():
		form.save()
	return redirect('/show')

def delete(request,id):
	users = Users.objects.get(id=id)
	users.delete()
	return redirect('/show')

