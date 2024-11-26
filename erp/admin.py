# Register your models here.


from django.contrib import admin
from .models import Employee
# Prevent re-registration
if not admin.site.is_registered(Employee):
    class EmployeeAdmin(admin.ModelAdmin):
        list_display = ('name', 'role', 'salary')

    admin.site.register(Employee, EmployeeAdmin)
    
# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ("name", "role", "salary")
#     search_fields = ("name", "role")
    
# admin.site.register(Employee, EmployeeAdmin)
