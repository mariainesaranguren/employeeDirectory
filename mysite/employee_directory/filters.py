import django_filters
from employee_directory.models import Employee

########## Creating and Declaring Filter Set

class EmployeeFilter(django_filters.FilterSet): ##Should this be in filters.py?
    class Meta:
        model = Employee
        fields =  {
            'name': ['icontains'],
            'team': ['iexact'],
            # 'start_date': ['gt']
        }
        # ['name', 'team'] #fields that will be filtered exactly
