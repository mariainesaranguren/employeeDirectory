#Will control the view here

from django.conf.urls import url
from . import views
from django_filters.views import FilterView

urlpatterns = [
	url(r'^$', views.employee_list),
	url(r'update', views.update_info),
	]
