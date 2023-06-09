# Generated by Django 4.2 on 2023-04-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_vacant_positions_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_report',
            name='work_date',
            field=models.DateTimeField(verbose_name='work_date'),
        ),
        migrations.AlterField(
            model_name='freelance_work',
            name='work_date',
            field=models.DateTimeField(verbose_name='work_date'),
        ),
        migrations.AlterField(
            model_name='main_report',
            name='vacant_end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='work_end_date'),
        ),
        migrations.AlterField(
            model_name='main_report',
            name='vacant_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='work_name'),
        ),
    ]
