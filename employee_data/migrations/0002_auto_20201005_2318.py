# Generated by Django 2.2.16 on 2020-10-05 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'verbose_name_plural': 'Data'},
        ),
        migrations.AlterField(
            model_name='data',
            name='employeeId',
            field=models.IntegerField(unique=True),
        ),
    ]
