# Generated by Django 4.2 on 2023-04-07 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_alter_main_report_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacant_positions',
            name='salary',
            field=models.FloatField(null=True, verbose_name='salary'),
        ),
    ]
