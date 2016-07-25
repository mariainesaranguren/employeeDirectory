from __future__ import unicode_literals
from django.db import models

from datetime import datetime #TODO Check if actually need this. Put it in for trials.

#Employee model using django

from django.db import models

class Employee(models.Model):
    # TODO: Add encoding somewhere to take care of non-ASCII characters
    name = models.CharField(max_length=60)
    # lastName = models.CharField(max_length=30)
    team = models.CharField(max_length=60)
    email = models.EmailField(max_length=25)
    phone_number = models.CharField(max_length=20)
    start_date = models.DateField(default=datetime.now, auto_now=False, auto_now_add=False) #??? TextInput?)
    title = models.CharField(max_length=30)
    created_at = models.DateField(auto_now=True, auto_now_add=False) #Automatically sets field to now when object is first created
    updated_at = models.DateField(auto_now=False, auto_now_add=True) #Automatically sets field to now when object is saved

    class Meta:
        app_label = 'webapp' #Declares which app the model belongs to
        db_table = 'webapp_employee' #Name of the database table for the model

    #Django separates you from actually writing any sql or any database information or language.
