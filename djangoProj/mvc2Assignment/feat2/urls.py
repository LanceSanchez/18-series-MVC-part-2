from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from feat2.models import Tenant
from . import views

urlpatterns = [
				url(r'^$', ListView.as_view(queryset=Tenant.objects.all().order_by("id"),template_name='view.html')),
			
				url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Tenant, template_name= 'view.html')),
				
				url(r'^/search$', views.search, name='search'),
				
				]