from django.shortcuts import render #Given but will not use this
from django.http import HttpResponse
from employee_directory.models import Employee
# Create your views here.

def index(request):
	context = {'results': Employee.objects.all()}
	return render(request, 'employee_table.html', context)
