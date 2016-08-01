#Will control the view here

from django.conf.urls import url
from . import views
from django_filters.views import FilterView

urlpatterns = [
	# url(r'^$', views.index, name='Index'),	# Will return view under def index() in views file (default view)
	url(r'^$', views.employee_list),
	]


# (r'^list/$', FilterView.as_view(model=Product)),
