# Generated by Django 4.1.5 on 2023-04-08 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0015_archival_report_alter_edit_report_work_date_end_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Directory_of_the_employees_location',
        ),
        migrations.RemoveField(
            model_name='staff_directory_employees',
            name='position',
        ),
    ]