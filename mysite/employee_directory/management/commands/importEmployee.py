from django.core.management.base import BaseCommand
import csv
from employee_directory.models import *
import calendar
import datetime
from datetime import date
import math

class Command(BaseCommand):
    help = "Test command - will be modified to import employee entries."

    def format_date_field(self, date_raw):
        day, month, year = date_raw.split("-")
        # Format year:
        year=int(year)
        # Format month:
        abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}
        month=abbr_to_num[month]
        # Format day:
        day=int(day)
        # Final format:
        date_final=datetime.date(year,month,day)
        return date_final

    def handle(self, *args, **options):
        with open('/Users/mariainesaranguren/Wizeline/mysite/newData3.csv') as csvfile:
            #TODO: Change path for csv file if moved or change at end (to not include my home directory)
            reader = csv.reader(csvfile)
            next(reader, None)  #Skip the headers
            for row in reader:

                # Parse start date. Given in day#-month-year#, must be in YYYY-MM-DD format.
                start_date_raw=row[7]
                if start_date_raw != '':
                    start_date_final = self.format_date_field(start_date_raw)
                else:
                    start_date_final = date.today()

                # Parse birth date
                birth_date_raw=row[6]
                if birth_date_raw != '':
                    birth_date_final = self.format_date_field(birth_date_raw)
                else:
                    birth_date_final = date.today()

                # Force set default photo if None
                if row[8]=='':
                    row[8]='employee_directory/NoPhotoDefault.gif'

                # Concatenate address
                if row [16] == 'Mexico':
                    # Street and Number, Neighborhood (Colonia), City, State, Country, "CP" Zip Code
                    address = '%s, %s, %s, %s, %s, CP %s' % (row[11], row[12], row[13], row[14], row[16], row[15])
                elif row[16] == 'USA' or row[17] == 'United States' or row[17] == 'United States of America':
                    # Street and Number, Neighborhood, City, State, Country, Zip Code
                    address = '%s, %s, %s, %s, %s, %s' % (row[11], row[12], row[13], row[14], row[16], row[15])
                else:
                    address = 'NA'
# Email ,First name,Last name,Team,Position,Manager,Birthdate,Age,Start Date,
#Image,Cell Phone Number,Personal Email,Street and Number,Neighborhood,City,State,Zip Code,Emergency Contact Info,Allergies,Blood Type,,,
                updated_values = {
                                  'first_name':row[1],
                                  'last_name':row[2],
                                  'full_name': '%s %s' % (row[1], row[2]),
                                  'team': row[3],
                                  'title': row[4],
                                  'manager': row[5],
                                  'birth_date': birth_date_final,
                                  'start_date': start_date_final,
                                  'image':  row[8],
                                  'phone_number': row[9],
                                  'personal_email': row[10],
                                  'address': address,
                                  'emergency_contact': row[17],
                                  'allergies': row[18],
                                  'blood_type': row[19]
                                  }

                employee, created = Employee.objects.update_or_create(email=row[0], defaults=updated_values)
                if created:
                    print 'New employee %s %s has been added.' % (employee.first_name, employee.last_name,)
                else:
                    print 'Employee %s %s has been updated.' % (employee.first_name, employee.last_name,)
                employee.save()
