from __future__ import unicode_literals

from django.db import models

# Create your models here.

#Django separates you from actually writing any sql or any database information or language. It's pretty high-level.

#Employee model using django

from django.db import models

class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=25)
    phoneNumber = models.IntegerField()
    # An integer. Values from -2147483648 to 2147483647 are safe in all databases supported by Django. The default form widget for this field is a NumberInput when localize is False or TextInput otherwise.
    # Muy chico? NumberInput?
    startDate = models.DateField(auto_now=False, auto_now_add=False) #??? TextInput?)
    title = models.CharField(max_length=30)
    createdAt = models.DateField(auto_now=True, auto_now_add=False) #Automatically sets field to now when object is first created
    updatedAt = models.DateField(auto_now=False, auto_now_add=True) #Automatically sets field to now when object is saved

    class Meta:
        app_label = 'myApp' #Declares which app the model belongs to
        db_table = 'employeeDatabase' #Name of the database table for the model



