from django.core.management.base import BaseCommand
import csv
from webapp.models import *

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

class Command(BaseCommand): #The class must be named Command, and subclass BaseCommand
    # Show this when the user types help
    help = "Test command - will be modified to import employee entries."

    # A command must define handle()
    def handle(self, *args, **options):
        #TODO: Try and except action here later ?
        # https://docs.djangoproject.com/en/1.9/howto/custom-management-commands/
        with open('/Users/mariainesaranguren/Wizeline/oldDirectory/Employee.csv') as csvfile:
            #TODO: Change path for csv file if moved or change at end (to not include my home directory)
            reader = csv.reader(csvfile)
            next(reader, None)  # skip the headers
            for row in reader:
                #TODO: Create Employee and save to database
                # import pdb; pdb.set_trace()

                #NAME, TEAM, POSITION, MANAGER, BIRTH DATE, AGE, START DATE
                #Parse start date. Given in day#-month-year#, must be in YYYY-MM-DD format.
                start_date_raw=row[6]
                test=select DATEPART(MM, start_date_raw)
                print test
                day, month, year=start_date_raw.split("-")
                year=int(year)
                # month=DASDASDASDA
                day=int(day)
                # print start_date_raw[1]
                #TODO: cast chars as ints

                # employee = Employee.objects.create(name=row[0], team=row[1], title=row[2], start_date=row[6]) #No phoneNumber
                # employee.save()
