from __future__ import unicode_literals
from django.db import models
from datetime import datetime
# from PIL import Image


class Employee(models.Model):
    # TODO: Add encoding somewhere to take care of non-ASCII characters ?
    name = models.CharField("Name", max_length=60)
    # lastName = models.CharField(max_length=30)
    # image = models.ImageField("Photo", upload_to='media', default='/Users/mariainesaranguren/Wizeline/mysite/media/default.jpeg')
    image = models.CharField("Photo", max_length=100, default="/Users/mariainesaranguren/Wizeline/mysite/media/default.jpeg")
    team = models.CharField("Team", max_length=60, default="NA")
    manager = models.CharField("Manager", max_length=60, default="NA")
    title = models.CharField("Title", max_length=40, default="NA")
    email = models.EmailField("Email", max_length=25, blank=True, null=True)
    phone_number = models.CharField("Phone Number", max_length=20)
    birth_date = models.DateField("Birth Date", default=datetime.now, auto_now=False, auto_now_add=False)
    age = models.IntegerField("Age", default=0)
    start_date = models.DateField("Start Date", default=datetime.now, auto_now=False, auto_now_add=False)
    created_at = models.DateField("Created at", auto_now=False, auto_now_add=True) #Automatically sets field to now when object is first created
    updated_at = models.DateField("Updated at", auto_now=True, auto_now_add=False) #Automatically sets field to now when object is saved

    class Meta:
        app_label = 'employee_directory' #Declares which app the model belongs to
        db_table = 'employee_directory_employee' #Name of the database table for the model
