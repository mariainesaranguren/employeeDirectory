# from django.shortcuts import render
# # from django.http import HttpResponse
# from employee_directory.models import Employee
# from employee_directory.tables import EmployeeTable
# from django_tables2 import RequestConfig
# # Create your views here.
#
# def index(request):
# # 	context = {'results': Employee.objects.all()}
# # 	return render(request, 'employee_table.html', context)
# # def people(request):
#     table = EmployeeTable(Employee.objects.all())
#     RequestConfig(request).configure(table) #Using RequestConfig automatically pulls values from request.GET and updates the table accordingly. This enables data ordering and pagination.
#     return render(request, 'employee_table.html', {'table': table})

from django.shortcuts import render
from employee_directory.models import Employee

def index(request):
    return render(request, 'employee_table.html', {'employees': Employee.objects.all()})
