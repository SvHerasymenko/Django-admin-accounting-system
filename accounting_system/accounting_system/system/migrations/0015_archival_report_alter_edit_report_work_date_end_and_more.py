# Generated by Django 4.1.5 on 2023-04-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0014_alter_edit_report_work_date_end_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archival_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_arcgival', models.DateField(verbose_name='date_archival')),
                ('employee_name', models.CharField(max_length=50, verbose_name='employee_name')),
                ('name_place_stay', models.CharField(max_length=100, verbose_name='name_place_stay')),
                ('work_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='work_name')),
                ('work_end_date', models.DateField(blank=True, null=True, verbose_name='work_end_date')),
            ],
        ),
        migrations.AlterField(
            model_name='edit_report',
            name='work_date_end',
            field=models.DateField(blank=True, null=True, verbose_name='work_date_end'),
        ),
        migrations.AlterField(
            model_name='freelance_work',
            name='work_date_end',
            field=models.DateField(verbose_name='work_date_end'),
        ),
        migrations.AlterField(
            model_name='main_report',
            name='work_end_date',
            field=models.DateField(blank=True, null=True, verbose_name='work_end_date'),
        ),
    ]