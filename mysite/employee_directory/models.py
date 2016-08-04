from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import django_filters

# from datetime import date
# from PIL import Image

########## Declaring Employee Model

class Employee(models.Model):
    # @property
    # def age(self):
    #     return self._my_date
    # @age.setter
    # def age(self, value):
    #     age_calc=today.year - self.year - ((today.month, today.day) < (self.month, self.day))
    #     self.age = age_calc

    def __unicode__(self):
       return self.last_name # Will display each employee's name in admin site, instead of "Employee object"

    # TODO: Add encoding somewhere to take care of non-ASCII characters ?
    # First argument is verbose name
    # blank=True means that field will not be required to create an entry
    # image = models.ImageField("Photo", upload_to='employee_directory', default='employee_directory/NoPhotoDefault.gif', blank=True)
    # image = models.CharField("Photo", max_length=100, default="/Users/mariainesaranguren/Wizeline/mysite/media/default.jpeg")
    first_name = models.CharField("First Name", max_length=30, default='NA')
    last_name = models.CharField("Last Name", max_length=30, default='NA')
    # name = models.CharField("Name", max_length=60)
    # lastName = models.CharField(max_length=30)
    email = models.EmailField("Email", max_length=40, blank=True, null=True)
    team = models.CharField("Team", max_length=60, blank=True)
    title = models.CharField("Title", max_length=40, blank=True)
    manager = models.CharField("Manager", max_length=60, blank=True)
    phone_number = models.CharField("Phone Number", max_length=20, blank=True)
    start_date = models.DateField("Start Date", default=datetime.now, blank=True, null=True) #default=datetime.now, auto_now=False, auto_now_add=False, blank=True)
    birth_date = models.DateField("Birth Date", default=datetime.now, blank=True, null=True)
    created_at = models.DateField("Created at", auto_now=False, auto_now_add=True) #Automatically sets field to now when object is first created
    updated_at = models.DateField("Updated at", auto_now=True, auto_now_add=False) #Automatically sets field to now when object is saved

    class Meta:
        app_label = 'employee_directory' #Declares which app the model belongs to
        db_table = 'employee_directory_employee' #Name of the database table for the model
