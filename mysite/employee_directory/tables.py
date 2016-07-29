import django_tables2 as tables
from employee_directory.models import Employee


class ImageColumn(tables.Column):
    def render(self, value):
        return mark_safe('<img src="{{MEDIA_ROOT}}/mysite/media/%s" height="50" />' % escape(value))
        # return mark_safe('<img src="http://kingofwallpapers.com/smile/smile-018.jpg" height="50" />' % escape(value))

class EmployeeTable(tables.Table):
    employee_pic = ImageColumn('Photo!!')
    # image = tables.Column(orderable=False)  #Restricts ordering for this column
    phone_number = tables.Column(orderable=False)
    email = tables.Column(orderable=False)
    class Meta:
        model = Employee
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        exclude = ('id', 'created_at', 'updated_at', ) #Hide id column
        # fields = ('name', 'image')
