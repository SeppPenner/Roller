# Generated by Django 2.2.16 on 2020-09-28 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0038_vehicle_vehicle_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclelocationtrack',
            name='suburb',
        ),
        migrations.DeleteModel(
            name='SubUrb',
        ),
    ]
