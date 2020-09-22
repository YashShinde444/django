# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm =  StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'addandshow.html',{'form':fm,'st':stud})
    #return HttpResponse("Hello")

def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(id=id)
        pi.delete()
        return HttpResponseRedirect('/add')

        