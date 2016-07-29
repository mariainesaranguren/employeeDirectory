#Will control the view here

from django.conf.urls import url
from . import views
from django_filters.views import FilterView

from .views import (
    EmployeeList,
    EmployeeDetail,
    EmployeeCreation,
    EmployeeUpdate,
    EmployeeDelete
)

urlpatterns = [
	# url(r'^$', views.index, name='Index'),	# Will return view under def index() in views file (default view)
	url(r'^$', views.employee_list),

	url(r'^$', EmployeeList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', EmployeeDetail.as_view(), name='detail'),
    url(r'^new$', EmployeeCreation.as_view(), name='new'),
    url(r'^edit/(?P<pk>\d+)$', EmployeeUpdate.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)$', EmployeeDelete.as_view(), name='delete'),
	]


# (r'^list/$', FilterView.as_view(model=Product)),
