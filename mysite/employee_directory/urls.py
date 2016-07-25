#Will control the view here

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index')] #Will return view under def index() in views file ("HEY!")
