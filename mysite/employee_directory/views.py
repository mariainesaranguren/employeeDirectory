from django.shortcuts import render
from django_tables2 import RequestConfig
from employee_directory.models import Employee
from employee_directory.tables import EmployeeTable
from employee_directory.filters import EmployeeFilter

from django.http import HttpResponseRedirect
from forms import UpdateForm
from django.core.mail import send_mail

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


def update_info(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UpdateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['maria.ines@wizeline.com'] #TODO Change to Claudia's email
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UpdateForm()

    f = EmployeeFilter(request.GET, queryset=Employee.objects.all())
    table = EmployeeTable(f.qs)
    RequestConfig(request, paginate={"per_page": 30, "page": 1}).configure(table)

    return render(request, 'employee_directory/update_form.html', {'form': form})
