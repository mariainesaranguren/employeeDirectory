from django.core.management.base import BaseCommand
import csv
from employee_directory.models import *
import calendar
import datetime
from datetime import date
import math

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

class Command(BaseCommand): #T he class must be named Command, and subclass BaseCommand
    # Show this when the user types help
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

    # A command must define handle()
    def handle(self, *args, **options):
        #TODO: Try and except action here later ?
        # https://docs.djangoproject.com/en/1.9/howto/custom-management-commands/
        with open('/Users/mariainesaranguren/Wizeline/mysite/oldDirectory/newData2.csv') as csvfile:
            #TODO: Change path for csv file if moved or change at end (to not include my home directory)
            reader = csv.reader(csvfile)
            next(reader, None)  #Skip the headers
            for row in reader:
                #TODO: Create Employee and save to database
                # Row: NAME, TEAM, POSITION, MANAGER, BIRTH DATE, AGE, START DATE
                # Parse start date. Given in day#-month-year#, must be in YYYY-MM-DD format.
                start_date_raw=row[8]
                print
                print 'start_date_raw', start_date_raw
                if start_date_raw != '':
                    start_date_final = self.format_date_field(start_date_raw)
                else:
                    start_date_final = date.today()
                # Parse birth date
                birth_date_raw=row[6]
                print 'birth_date_raw', birth_date_raw
                if birth_date_raw != '':
                    birth_date_final = self.format_date_field(birth_date_raw)
                else:
                    birth_date_final = date.today()

                # Set values
                updated_values = {
                                #   'name':row[3],
                                  'first_name':row[1],
                                  'last_name':row[2],
                                  'team': row[3],
                                  'title': row[4],
                                  'manager': row[5],
                                  'birth_date': birth_date_final,
                                #   'age': int(math.floor(float(row[8]))),
                                  'start_date': start_date_final,
                                  'image':  row[9]}
                print 'email:', row[0]

                print birth_date_final
                print start_date_final

                employee, created = Employee.objects.update_or_create(email=row[0], defaults=updated_values)
                if created:
                    print 'New employee %s has been added.' % (employee.last_name,)
                else:
                    print 'Employee %s has been updated ' % (employee.last_name,)
                employee.save()


# import pdb; pdb.set_trace()
