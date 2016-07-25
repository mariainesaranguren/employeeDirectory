from django.core.management.base import BaseCommand
import csv
from webapp.models import *
import calendar
import datetime
import math

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

class Command(BaseCommand): #The class must be named Command, and subclass BaseCommand
    # Show this when the user types help
    help = "Test command - will be modified to import employee entries."

    def format_date_field(self, date_raw):
        day, month, year = date_raw.split("-")
        #Format year:
        year=int(year)
        #Format month:
        abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}
        month=abbr_to_num[month]
        #Format day:
        day=int(day)
        #Final format:
        date_final=datetime.date(year,month,day)
        return date_final

    # A command must define handle()
    def handle(self, *args, **options):
        #TODO: Try and except action here later ?
        # https://docs.djangoproject.com/en/1.9/howto/custom-management-commands/
        with open('/Users/mariainesaranguren/Wizeline/oldDirectory/Employee.csv') as csvfile:
            #TODO: Change path for csv file if moved or change at end (to not include my home directory)
            reader = csv.reader(csvfile)
            next(reader, None)  #Skip the headers TODO: still showing up on database, fix.
            for row in reader:
                #TODO: Create Employee and save to database
                # import pdb; pdb.set_trace()
                #Row: NAME, TEAM, POSITION, MANAGER, BIRTH DATE, AGE, START DATE
                #Parse start date. Given in day#-month-year#, must be in YYYY-MM-DD format.
                start_date_raw=row[6]
                start_date_final=self.format_date_field(start_date_raw)
                #Parse birth date
                birth_date_raw=row[4]
                birth_date_final=self.format_date_field(birth_date_raw)
                employee = Employee.objects.create(name=row[0], team=row[1], title=row[2], manager=row[3], birth_date=birth_date_final, age=int(math.floor(float(row[5]))), start_date=start_date_final, email=row[7]) #No phoneNumber
                # employee.save()
