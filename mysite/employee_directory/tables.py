import django_tables2 as tables
from employee_directory.models import Employee
from django.utils.html import format_html

class ImageColumn(tables.Column):
    def render(self, value):
        return format_html('<img src="/media/{}" height="100" width="100"/>', value)

class EmployeeTable(tables.Table):
    image = ImageColumn(orderable=False)  #Restricts ordering for this column
    email = tables.Column(orderable=False)
    title = tables.Column(orderable=False)
    manager = tables.Column(orderable=False)
    phone_number = tables.Column(orderable=False)

    class Meta:
        model = Employee
        attrs = {'class': 'table table-striped table-hover'}
        exclude = ('id',    #Hide columns
                  'first_name',
                  'last_name',
                  'start_date',
                  'address',
                  'personal_email',
                  'birth_date',
                  'blood_type',
                  'allergies',
                  'emergency_contact',
                  'created_at',
                  'updated_at',
        )
