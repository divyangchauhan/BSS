# Generated by Django 3.1.1 on 2020-09-30 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Billing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='bill_id',
        ),
    ]
