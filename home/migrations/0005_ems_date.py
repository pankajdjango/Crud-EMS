# Generated by Django 3.2.4 on 2021-07-10 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_ems_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='ems',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
