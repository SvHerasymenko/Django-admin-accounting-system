# Generated by Django 4.1.5 on 2023-04-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_rename_vacant_end_date_main_report_work_end_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edit_report',
            name='work_date',
        ),
        migrations.RemoveField(
            model_name='freelance_work',
            name='work_date',
        ),
        migrations.AddField(
            model_name='edit_report',
            name='work_date_end',
            field=models.DateTimeField(null=True, verbose_name='work_date_end'),
        ),
        migrations.AddField(
            model_name='freelance_work',
            name='work_date_end',
            field=models.DateTimeField(null=True, verbose_name='work_date_end'),
        ),
    ]