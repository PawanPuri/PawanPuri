from django.contrib import admin

# Register your models here.
from testapp.models import Emp_model
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']
admin.site.register(Emp_model,EmployeeAdmin)

