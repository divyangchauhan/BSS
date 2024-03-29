# Generated by Django 3.1.1 on 2020-09-30 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Battery', '0001_initial'),
        ('Station', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=200, unique=True)),
                ('transaction_start_time', models.DateTimeField()),
                ('transaction_stop_time', models.DateTimeField()),
                ('transaction_day', models.DateField()),
                ('battery_state_in', models.IntegerField()),
                ('battery_state_out', models.IntegerField()),
                ('Battery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Battery.battery')),
                ('Station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Station.station')),
            ],
        ),
    ]
