from django.http import HttpResponse
from django.template import loader
from feat2.models import Tenant
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

def search(request):
	if request.method == 'POST':
		searched = request.POST.get('search', 'None')
		print searched
		results = Tenant.objects.filter(Q(fname__contains=searched) | Q(mname__contains=searched) | Q(lname__contains=searched) | Q(sex__contains=searched) | Q(addressHome__contains=searched) | Q(course__contains=searched) | Q(birth_date__contains=searched))
		
		return render(request, 'view_search.html', {'results':results})
		
	return render(request, 'view.html')