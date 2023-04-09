from django.db.models.signals import post_save,post_delete,pre_save
from django.core.signals import request_started, request_finished
from django.dispatch import receiver
from loguru import logger
from system.models import Staff_directory_employees,Main_report,Edit_report,Archival_report,Directory_of_positions,Vacant_positions,Freelance_work
import datetime
from datetime import date

logger.add('logs/signal.log', format='{time} {level} {message}')

@receiver(post_save, sender=Staff_directory_employees)
@logger.catch
def check_employees_data(sender, **kwargs):
    for employees in Staff_directory_employees.objects.all():
        if str(employees) in Main_report.objects.all().values_list("employee_name", flat=True):
            pass
        else:
            unit= Main_report(employee_name = f"{employees}",name_place_stay= "at disposal" )
            unit.save()

@receiver(post_delete, sender=Staff_directory_employees)
@logger.catch
def delete_employees(sender, **kwargs):
    for del_employees in Main_report.objects.all():
        print(del_employees)
        if str(del_employees) in Staff_directory_employees.objects.all().values_list("full_name",flat=True):
            pass
        else:
            del_p1 = Main_report.objects.get(employee_name= f"{del_employees}")
            del_p1.delete()
            del_p2 =Edit_report.objects.get(employee_name= f"{del_employees}")
            del_p2.delete()

@receiver(post_save, sender=Staff_directory_employees)
@logger.catch
def edit_main_report(sender, **kwargs):
    for employees in Staff_directory_employees.objects.all():
        if str(employees) in Edit_report.objects.all().values_list("employee_name", flat=True):
            pass
        else:
            worker= Edit_report(employee_name = f"{employees}")
            worker.save()
    
@receiver(post_save, sender=Edit_report)
@logger.catch
def edit_reports(sender, **kwargs):
    for unit in Edit_report.objects.all():
        employ = Main_report.objects.get(employee_name= f"{unit}")
        employ.work_name = str(Edit_report.objects.get(employee_name=f"{unit}").work_name)
        if employ.work_name ==str (None):
            employ.name_place_stay = "at disposal"
        else:
            employ.name_place_stay = "at work"
        employ.work_end_date = Edit_report.objects.get(employee_name=f"{unit}").work_date_end
        employ.save()

@receiver(request_started)
@logger.catch
def check_datetime(sender, **kwargs):
    for unit in Edit_report.objects.all():
        datetime_db = Edit_report.objects.get(employee_name = unit).work_date_end
        if datetime_db !=None:
            today = date.today()
            if datetime_db <= today:
                workman = Edit_report.objects.get(employee_name= f"{unit}")
                workman.work_date_end = None
                workman.work_name = None
                workman.save()
                user = Main_report.objects.get(employee_name= f"{unit}")
                user.name_place_stay = "at disposal"
                user.save()

@receiver(request_finished)
@logger.catch
def archival_data(sender, **kwargs):
    now = datetime.datetime.now()
    h_day = now + datetime.timedelta(hours=19)
    next_day = now + datetime.timedelta(days=1)
    if next_day.strftime("%Y-%m-%d") == h_day.strftime("%Y-%m-%d"):
        if date.today() in Archival_report.objects.all().values_list("date_arcgival",flat=True):
            pass
        else:
            for unit in Edit_report.objects.all():
                employ = Main_report.objects.get(employee_name= f"{unit}")
                archival = Archival_report(date_arcgival = date.today(),employee_name = employ.employee_name, name_place_stay= employ.name_place_stay, work_name = employ.work_name, work_end_date = employ.work_end_date)               
                archival.save()

@receiver(post_save,sender=Directory_of_positions)
@logger.catch
def position(sender, **kwargs):
    for positions in Directory_of_positions.objects.all():
        if str(positions) in Staff_directory_employees.objects.all().values_list("position", flat=True) or str(positions) in Vacant_positions.objects.all().values_list("name_vacant_position", flat=True):
            print("this position was created")
        else:
            vacant= Vacant_positions(name_vacant_position= f"{positions}", salary= Directory_of_positions.objects.get(full_position_name =f"{positions}").salary )
            vacant.save()
