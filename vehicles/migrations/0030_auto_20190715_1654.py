# Generated by Django 2.2.3 on 2019-07-15 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0029_auto_20190715_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publictransportstation',
            old_name='point',
            new_name='position',
        ),
    ]