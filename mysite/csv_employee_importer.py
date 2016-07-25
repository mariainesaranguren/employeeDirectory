import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import csv
from webapp.models import *

with open('/Users/mariainesaranguren/Wizeline/oldDirectory/Employee.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        #TODO: Create Employee and save to database
        import pdb; pdb.set_trace()
        print row
