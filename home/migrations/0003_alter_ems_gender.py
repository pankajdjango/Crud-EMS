# Generated by Django 3.2.4 on 2021-07-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210710_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ems',
            name='gender',
            field=models.CharField(choices=[('Male', 'Female')], max_length=10),
        ),
    ]
