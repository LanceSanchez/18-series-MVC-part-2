from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from feat3.models import Tenant
from . import views

urlpatterns = [
			
				url(r'(?P<pk>[0-9]+)$', views.delete, name='delete'),
			
				
			  ]