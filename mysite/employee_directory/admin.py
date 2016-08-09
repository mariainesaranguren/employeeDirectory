# ModelAdmin classes exist for each model that is editable in the django admin interface.
# This class encapsulates the customized admin functionality and options for each particular model.

from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Employee

admin.site.site_header = "Wizeline Employee Directory Administration"
admin.site.site_title = "Wizeline Employee Directory"
admin.site.index_title = "Index"

class MyAdminSite(AdminSite):
    site_header = 'Wizeline Employee Directory Administration'
admin_site = MyAdminSite(name='admin')

class EmployeeAdmin(admin.ModelAdmin):
    # def linked_first_name(self, employee):
    #     if employee.first_name:
    #         # change_employee_directory_page = 'admin:%s_%s_change' % (employee._meta.app_label, employee._meta.module_name)
    #         url = reverse(change_employee_directory_page, args=(employee.employee_directory.id,))
    #         return format_html(u'<a href="{}">{}</a>', url, employee.employee_directory.first_name)
    #     return ''
    # linked_first_name.short_description = 'First name'

    list_display = (
        'id',
        'image',
        # 'admin_image',
        # 'linked_first_name',
        'first_name',
        'last_name',
        'title',
        'team',
        'manager',
        'email',
        # 'phone_number',
        # 'start_date',
        # 'address',
        # 'personal_email',
        # 'birth_date',
        # 'blood_type',
        # 'allergies',
        # 'emergency_contact',
        # 'created_at',
        # 'updated_at'
    )
    list_filter = (
        'team',
        'title',
    )
    search_fields = ['first_name', 'last_name']
    ordering = ('first_name',) # Set default ordering to A-Z by first_name
    # change_form_template = 'admin/change_form.html'


admin.site.register(Employee, EmployeeAdmin)
