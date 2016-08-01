"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include # Added include for added urlpatterns
from django.contrib import admin
from django.contrib.auth import views as auth_views # To reset passwords in admin
admin.autodiscover() # This function attempts to import an admin module in each installed application. Such modules are expected to register models with the admin.
from employee_directory.admin import admin_site #For admin site

urlpatterns = [
    # url(r'^admin/', admin.site.urls), #Can think of this as it's own app
    # url(r'^admin/', admin_site.urls),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('employee_directory.urls')), # Includes webapp.urls.py file. When someone goes to webapp on website, this tells it it needs to go to webapp.urls to figure out the view it has to provide
    #Removed $
    url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'), #Password reset
    url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete')
]
