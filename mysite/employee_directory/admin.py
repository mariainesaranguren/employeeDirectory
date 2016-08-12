# ModelAdmin classes exist for each model that is editable in the django admin interface.
# This class encapsulates the customized admin functionality and options for each particular model.

from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Employee
from django.forms import ModelForm

admin.site.site_header = "Wizeline Employee Directory Administration"
admin.site.site_title = "Wizeline Employee Directory"
admin.site.index_title = "Index"

class MyAdminSite(AdminSite):
    site_header = 'Wizeline Employee Directory Administration'
admin_site = MyAdminSite(name='admin')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'title',
        'team',
        'manager',
        'email',
    )
    list_filter = (
        'team',
        'title',
    )
    search_fields = ['first_name', 'last_name']
    ordering = ('first_name',) # Set default ordering to A-Z by first_name

admin.site.register(Employee, EmployeeAdmin)
