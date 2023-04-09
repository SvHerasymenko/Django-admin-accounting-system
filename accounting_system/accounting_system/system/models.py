from django.db import models


class Directory_of_positions(models.Model):
    position = models.CharField('position', max_length=50)
    partition = models.CharField('partition' ,max_length=50)
    filial = models.CharField('filial', max_length=50)
    squad = models.CharField('squad', max_length = 50)
    department = models.CharField('department', max_length=50)
    full_position_name = models.CharField('full_position_name',max_length=50)
    staff_rank = models.CharField('staff_rank',max_length=50)
    staff_position_number = models.CharField('staff_position_number', max_length=50)
    salary = models.FloatField('salary')

    def __str__(self):
        return self.full_position_name
    
    class Meta:
        verbose_name = "Directory_of_position"

class Vacant_positions(models.Model):
    name_vacant_position = models.CharField('vacant_name',max_length=50)
    salary = models.FloatField('salary',null=True)

    def __str__(self):
        return self.name_vacant_position

class Staff_directory_employees(models.Model):
    full_name = models.CharField('full_name',max_length=100)
    staff_number =models.IntegerField('staff_number')
    date_of_birth = models.DateField('date_of_birth')
    cellphone = models.IntegerField('cellphone')
    place_of_birth =models.CharField('place_of_birth',max_length=100)
    address_of_actual_residence =models.TextField('address_of_actual_residence',max_length=100)
    enrollment_date =models.DateField('enrollment_date')
    actual_rank= models.CharField('actual_rank',max_length=50)
    username= models.CharField('username',max_length=50)
    reference_information = models.TextField('reference information',max_length=150)
    position = models.OneToOneField(Vacant_positions, on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
         verbose_name = "Staff_directory_employee"

class Main_report(models.Model):
    employee_name = models.CharField('employee_name',max_length=50)
    name_place_stay = models.CharField('name_place_stay',max_length=100)
    work_name = models.CharField('work_name',max_length=50,null=True,blank=True)
    work_end_date = models.DateField('work_end_date',null=True,blank=True)

    def __str__(self):
        return self.employee_name

    class Meta:
         verbose_name = "Main_report"
         verbose_name_plural = "Main_report"

class Freelance_work(models.Model):
    work_name = models.CharField('work_name',max_length=50)
    work_date_end = models.DateField('work_date_end')

    def __str__(self):
        return self.work_name

class Edit_report(models.Model):
    employee_name = models.CharField('employee_name',max_length=50)
    work_name = models.OneToOneField(Freelance_work,on_delete=models.SET_NULL,null=True,blank=True)
    work_date_end = models.DateField('work_date_end',null=True,blank=True)

    def __str__(self):
        return self.employee_name

class Archival_report(models.Model):
    date_arcgival = models.DateField('date_archival')
    employee_name = models.CharField('employee_name',max_length=50)
    name_place_stay = models.CharField('name_place_stay',max_length=100)
    work_name = models.CharField('work_name',max_length=50,null=True,blank=True)
    work_end_date = models.DateField('work_end_date',null=True,blank=True)