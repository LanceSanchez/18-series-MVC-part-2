from django.http import HttpResponse
from django.template import loader
from feat2.models import Tenant
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


def delete(request, pk):
	
	if request.method == 'POST':
		Tenant.objects.filter(id=int(request.POST.get('Store','None'))).delete()

		return HttpResponseRedirect('/view')
	return render(request, 'view.html')