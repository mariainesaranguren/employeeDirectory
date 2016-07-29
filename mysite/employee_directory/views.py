# from django.shortcuts import render
# # from django.http import HttpResponse
# from employee_directory.models import Employee
# from employee_directory.tables import EmployeeTable
# from django_tables2 import RequestConfig
# # Create your views here.
#
# def index(request):
# #     context = {'results': Employee.objects.all()}
# #     return render(request, 'employee_table.html', context)
# # def people(request):
#     table = EmployeeTable(Employee.objects.all())
#     RequestConfig(request).configure(table) #Using RequestConfig automatically pulls values from request.GET and updates the table accordingly. This enables data ordering and pagination.
#     return render(request, 'employee_table.html', {'table': table})

from django.shortcuts import render
from django_tables2 import RequestConfig
from employee_directory.models import Employee
from employee_directory.tables import EmployeeTable
from employee_directory.filters import EmployeeFilter

#Default view
def index(request):
    # return render(request, 'employee_table.html', {'employees': Employee.objects.all()})
    table = EmployeeTable(Employee.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'employee_directory/employee_table.html', {'table': table})

#Filtering view
def employee_list(request):
    f = EmployeeFilter(request.GET, queryset=Employee.objects.all())
    table = EmployeeTable(f.qs)
    RequestConfig(request, paginate={"per_page": 30, "page": 1}).configure(table)
    return render(request, 'employee_directory/filtering.html', {'filter': f, 'table': table})


# queryset = Fitzroyfalls.objects.select_related().all()
# f = FitzroyfallsFilter(request.GET, queryset=queryset)
# table = FitsroyFallsTable(f.qs)
# RequestConfig(request, paginate={"per_page": 25, "page": 1}).configure(table)
# return render(request, 'query.html', {'table': table, 'filter': f})
