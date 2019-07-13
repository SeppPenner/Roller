# Generated by Django 2.2.3 on 2019-07-13 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0008_auto_20190713_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unlock_fee', models.DecimalField(decimal_places=3, max_digits=5)),
                ('minute_price', models.DecimalField(decimal_places=3, max_digits=5)),
                ('service_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.ServiceTrackingArea')),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.ServiceProvider')),
            ],
        ),
    ]