import django_tables2 as tables
from employee_directory.models import Employee

class EmployeeTable(tables.Table):
    class Meta:
        model = Employee
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
