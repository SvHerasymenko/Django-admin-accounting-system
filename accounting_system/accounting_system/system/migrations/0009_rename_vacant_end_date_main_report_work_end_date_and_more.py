# Generated by Django 4.2 on 2023-04-07 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_alter_edit_report_work_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main_report',
            old_name='vacant_end_date',
            new_name='work_end_date',
        ),
        migrations.RenameField(
            model_name='main_report',
            old_name='vacant_name',
            new_name='work_name',
        ),
    ]