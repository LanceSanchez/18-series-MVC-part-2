from django.http import HttpResponse
from django.template import loader
from feat2.models import Tenant
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


def update(request, pk):
	tenants = Tenant.objects.get(id=int(pk))
	
	if request.method == 'POST':
		tenant = Tenant.objects.get(id=int(pk))
		tenant.fname = request.POST.get('fname','None')
		tenant.mname = request.POST.get('mname','None')
		tenant.lname = request.POST.get('lname','None')
		tenant.sex = request.POST.get('sex','None')
		tenant.addressHome = request.POST.get('address','None')
		tenant.course = request.POST.get('course','None')
		tenant.birth_date = request.POST.get('birthdate','2018-03-11')

		tenant.save()

		return HttpResponseRedirect('http://127.0.0.1:8000/view')
		
	return render(request, 'update.html', {'tenants':tenants,'pk': pk})
