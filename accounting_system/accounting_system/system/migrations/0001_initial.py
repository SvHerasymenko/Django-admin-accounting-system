# Generated by Django 4.2 on 2023-04-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directory_of_positions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partition', models.CharField(max_length=50, verbose_name='partition')),
                ('filial', models.CharField(max_length=50, verbose_name='filial')),
                ('squad', models.CharField(max_length=50, verbose_name='squad')),
                ('department', models.CharField(max_length=50, verbose_name='department')),
                ('position', models.CharField(max_length=50, verbose_name='position')),
                ('full_position_name', models.CharField(max_length=50, verbose_name='full_position_name')),
                ('staff_rank', models.CharField(max_length=50, verbose_name='staff_rank')),
                ('staff_position_number', models.CharField(max_length=50, verbose_name='staff_position_number')),
                ('salary', models.FloatField(verbose_name='salary')),
            ],
            options={
                'verbose_name': 'Directory_of_position',
            },
        ),
    ]