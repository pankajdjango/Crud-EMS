# Generated by Django 3.2.4 on 2021-07-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_ems_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ems',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]
