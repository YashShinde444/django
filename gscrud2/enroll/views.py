# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView,RedirectView
from django.views import View
# Create your views here.

class UserAddShowView(TemplateView):
    template_name='addandshow.html'
    def get_context_data(self, *args , **kwargs):
        context = super(UserAddShowView,self).get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context = {'st':stud,'form':fm}
        return context

    def post(self,request):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/add')


'''def add_show(request):
    if request.method == 'POST':
        fm =  StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'addandshow.html',{'form':fm,'st':stud})
    #return HttpResponse("Hello")'''

class UserDeleteView(RedirectView):
    url = '/add'
    def get_redirect_url(self,*args,**kwargs):
        print(kwargs)
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super(UserDeleteView,self).get_redirect_url(*args,**kwargs)

'''def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(id=id)
        pi.delete()
        return HttpResponseRedirect('/add')'''

class UserUpdateView(View):
    def get(self,request,id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request,'updatestudent.html',{'form':fm})

    def post(self,request,id):
        pi=User.objects.get(pk=id)
        fm =  StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return render(request,'updatestudent.html',{'form':fm})
