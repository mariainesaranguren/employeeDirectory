# ModelAdmin classes exist for each model that is editable in the django admin interface.
# This class encapsulates the customized admin functionality and options for each particular model.

from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Employee

# from datetime import date

# from django.http import HttpResponse
# from django.core import serializers

admin.site.site_header = "Wizeline Employee Directory Administration"
admin.site.site_title = "Wizeline Employee Directory"
admin.site.index_title = "Index"

class MyAdminSite(AdminSite):
    site_header = 'Wizeline Employee Directory Administration'
admin_site = MyAdminSite(name='admin')
# admin_site.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]
    # list_display = ('image', 'first_name', 'last_name', 'team', 'title', 'manager','email', 'phone_number', 'birth_date')
    ordering = ('first_name',) # Set default ordering to A-Z by first_name
    exclude = ('age',) # TODO set up for age to be set automatically with birth_date
    actions = ['delete']
    # change_form_template = 'wize_admin.html'
    # pass
    css = {
             'all': ('admin/wizeline-admin.css',)
        }

admin.site.register(Employee, EmployeeAdmin) # Not needed because below replaces default admin site.
