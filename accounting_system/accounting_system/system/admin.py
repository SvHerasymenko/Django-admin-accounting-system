import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accounting_system.settings')

from django.core.management.base import BaseCommand
from django.contrib import admin
from system.models import Directory_of_positions,Staff_directory_employees,Main_report,Vacant_positions,Freelance_work,Edit_report,Archival_report
# Register your models here.

@admin.register(Main_report)
class Main_report(admin.ModelAdmin):
    list_display =['employee_name','name_place_stay','work_name','work_end_date']
    readonly_fields =['name_place_stay','work_name','work_end_date']

@admin.register(Staff_directory_employees,Directory_of_positions,Freelance_work)
class Adminsas(admin.ModelAdmin):
    pass

@admin.register(Vacant_positions)
class Vacant_position(admin.ModelAdmin):
    list_display= ['name_vacant_position','salary']

@admin.register(Edit_report)
class Edit_report(admin.ModelAdmin):
    list_display =['employee_name','work_name', 'work_date_end']
    list_editable = ['work_name', 'work_date_end']

@admin.register(Archival_report)
class Archival_report(admin.ModelAdmin):
    list_display = ['date_arcgival','employee_name','name_place_stay','work_name','work_end_date']
    readonly_fields =['date_arcgival','employee_name','name_place_stay','work_name','work_end_date']
    ordering = ['-date_arcgival', '-employee_name']