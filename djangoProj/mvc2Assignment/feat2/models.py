from __future__ import unicode_literals

from django.db import models
import datetime

class Tenant(models.Model):
	idnum = models.CharField(max_length=9)
	fname = models.CharField(max_length=60)
	mname = models.CharField(max_length=60)
	lname = models.CharField(max_length=60)
	sex = models.CharField(max_length=6)
	addressHome = models.CharField(max_length=60)
	course = models.CharField(max_length=60)
	birth_date = models.DateField(null=False)




	def __str__(self):
		return self.idnum







