import django_filters
from employee_directory.models import Employee

########## Creating and Declaring Filter Set

class EmployeeFilter(django_filters.FilterSet): ##Should this be in filters.py?
    name = django_filters.CharFilter(lookup_expr='icontains')
    team = django_filters.CharFilter(lookup_expr='icontains')

    # price = django_filters.NumberFilter()
    # price__gt = django_filters.NumberFilter(name='price', lookup_expr='gt')
    # price__lt = django_filters.NumberFilter(name='price', lookup_expr='lt')
    #
    # release_year = django_filters.NumberFilter(name='release_date', lookup_expr='year')
    # release_year__gt = django_filters.NumberFilter(name='release_date', lookup_expr='year__gt')
    # release_year__lt = django_filters.NumberFilter(name='release_date', lookup_expr='year__lt')

    class Meta:
        model = Employee
        # fields = ['name', 'team'] #fields that will be filtered exactly
