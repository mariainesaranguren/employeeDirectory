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
        #TODO: Try and except action here later
        # https://docs.djangoproject.com/en/1.9/howto/custom-management-commands/

        self.stdout.write("dasdasds!")
        with open('/Users/mariainesaranguren/Wizeline/oldDirectory/Employee.csv') as csvfile:
            #TODO: Change path for csv file
            self.stdout.write("HERE")
            reader = csv.reader(csvfile)
            for row in reader:
                #TODO: Create Employee and save to database
                # import pdb; pdb.set_trace()
                print row
