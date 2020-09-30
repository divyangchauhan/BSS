# Generated by Django 3.1.1 on 2020-09-30 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=20, unique=True)),
                ('company_city', models.CharField(max_length=20)),
                ('company_state', models.CharField(max_length=20)),
                ('company_country', models.CharField(choices=[('India', 'India'), ('USA', 'US'), ('UK', 'UK')], default='India', max_length=20)),
            ],
        ),
    ]
