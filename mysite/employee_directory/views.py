from django.shortcuts import render #Given but will not use this
from django.http import HttpResponse

# Create your views here.

def index(request):
	# return HttpResponse("<h2>HEY!</h2>")
	# dictionary = {'obj': models.Employee.objects.all()}
	return render(request, '/Users/mariainesaranguren/Wizeline/mysite/employee_directory/templates/employee_directory/employee_table.html')
