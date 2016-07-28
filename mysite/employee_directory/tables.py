import django_tables2 as tables
from employee_directory.models import Employee

class EmployeeTable(tables.Table):
    image = tables.Column(orderable=False)  #Restricts ordering for this column
    phone_number = tables.Column(orderable=False)
    email = tables.Column(orderable=False)
    class Meta:
        model = Employee
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        exclude = ('id',) #Hide id ccolumn
