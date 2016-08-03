import django_filters
from employee_directory.models import Employee
# from django.db.models import Q

########## Creating and Declaring Filter Set

class EmployeeFilter(django_filters.FilterSet):
    full_name = django_filters.MethodFilter()
    global_search = django_filters.MethodFilter()
    team = django_filters.MethodFilter()

    def filter_full_name(self, queryset, value):
        if value:
            return queryset.filter(first_name__icontains=value) | queryset.filter(last_name__icontains=value)
        return queryset

    def filter_global_search(self, queryset, value):
        if value:
            return (queryset.filter(first_name__icontains=value)
                   | queryset.filter(last_name__icontains=value)
                   | queryset.filter(email__icontains=value)
                   | queryset.filter(team__icontains=value)
                   | queryset.filter(title__icontains=value)
                   | queryset.filter(manager__icontains=value)
                   | queryset.filter(phone_number__icontains=value)
                   | queryset.filter(start_date__icontains=value)
                   | queryset.filter(birth_date__icontains=value)
                   | queryset.filter(created_at__icontains=value)
                   | queryset.filter(updated_at__icontains=value))
        return queryset

    def filter_team(self, queryset, value):
        if value:
            return queryset.filter(team__icontains=value)
        return queryset

    class Meta:
        model = Employee
        fields =  {
            'global_search',
            'full_name',
            'team'
        }
