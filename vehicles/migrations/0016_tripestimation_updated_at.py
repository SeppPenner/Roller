# Generated by Django 2.2.3 on 2019-07-13 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0015_auto_20190713_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripestimation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]