from django.contrib import admin
from paytm1.models import Employee
from paytm1.models import JobData


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal','eaddr']

class JobAdmin(admin.ModelAdmin):
    list_display = ['jposting','jlocation','joffersal','jquali']


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(JobData,JobAdmin)



