from django.http import HttpResponse
from django.template import loader
from feat2.models import Tenant
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


def add(request):
	if request.method == 'POST':
		tenant = Tenant()
		tenant.idnum = request.POST.get('idnum', 'None')
		tenant.fname = request.POST.get('fname','None')
		tenant.mname = request.POST.get('mname','None')
		tenant.lname = request.POST.get('lname','None')
		tenant.sex = request.POST.get('sex','None')
		tenant.addressHome = request.POST.get('address','None')
		tenant.course = request.POST.get('course','None')
		tenant.birth_date = request.POST.get('birthdate','2018-03-11')
		next = request.POST.get('next','/')
		tenant.save()

		return HttpResponseRedirect('add/success')
		
	return render(request,'add.html')

	
def success(request):
	
	
	return render(request, 'success.html')