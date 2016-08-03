from django.shortcuts import render
from django_tables2 import RequestConfig
from employee_directory.models import Employee
from employee_directory.tables import EmployeeTable
from employee_directory.filters import EmployeeFilter

# #Default view
# def index(request):
#     # return render(request, 'employee_table.html', {'employees': Employee.objects.all()})
#     table = EmployeeTable(Employee.objects.all())
#     RequestConfig(request).configure(table)
#     return render(request, 'employee_directory/employee_table.html', {'table': table})


# Default view
def employee_list(request):
    f = EmployeeFilter(request.GET, queryset=Employee.objects.all())
    table = EmployeeTable(f.qs)
    RequestConfig(request, paginate={"per_page": 30, "page": 1}).configure(table)
    return render(request, 'employee_directory/filtering.html', {'filter': f, 'table': table})
