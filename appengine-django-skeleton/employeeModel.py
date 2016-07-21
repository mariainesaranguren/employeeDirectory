#!/usr/bin/env python2.7

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

# Esto donde tiene que ir?
# employee1 = Employee(
#     firstName="Nombre", lastName="Apellido", email="nombre@wizeline.com", phoneNumber=2323242, title="Software Engineer").save() # Saves object to database
# employee2 = Employee(
#     firstName="Nombre2", lastName="Apellido2", email="nombre2@wizeline.com", phoneNumber=232324223131, title="Software Engineer2").save() # Saves object to database
# employee3 = Employee(
#     firstName="Nombre3", lastName="Apellido3", email="nombre3@wizeline.com", phoneNumber=33333323131, title="Software Engineer3").save() # Saves object to database


# CREATE TABLE testDatabase.db_table (
#     "id" serial NOT NULL PRIMARY KEY,
#     "firstName" varchar(30) NOT NULL,
#     "lastName" varchar(30) NOT NULL,
#     "email" varchar(30) NOT NULL,
#     # "phoneNumber"
#
# );


# Field Info https://docs.djangoproject.com/en/1.9/ref/models/fields/#django.db.models.Field
