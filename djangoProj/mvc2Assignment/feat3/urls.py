from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from feat3.models import Tenant
from . import views

urlpatterns = [
			
				url(r'^$', views.add, name='add'),
				url(r'success$', views.success, name='success'),
				
			  ]