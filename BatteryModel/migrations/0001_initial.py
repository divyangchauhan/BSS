# Generated by Django 3.1.1 on 2020-09-30 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battery_model_id', models.CharField(max_length=100)),
                ('battery_model_capacity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('battery_model_current', models.DecimalField(decimal_places=10, max_digits=20)),
                ('battery_model_voltage', models.DecimalField(decimal_places=10, max_digits=20)),
                ('battery_model_width', models.DecimalField(decimal_places=10, max_digits=20)),
                ('battery_model_length', models.DecimalField(decimal_places=10, max_digits=20)),
                ('battery_model_height', models.DecimalField(decimal_places=10, max_digits=20)),
                ('battery_model_oem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.company')),
            ],
        ),
    ]