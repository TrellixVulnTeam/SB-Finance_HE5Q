# Generated by Django 2.2.3 on 2019-07-12 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=16, verbose_name='First name')),
                ('last_name', models.CharField(max_length=16, verbose_name='Last name')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('phone1', models.IntegerField()),
                ('phone2', models.IntegerField()),
                ('date_of_birth', models.DateField(default=None, verbose_name='Date of Birth')),
            ],
        ),
        migrations.CreateModel(
            name='Payslip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('basic_pay', models.IntegerField(default=0)),
                ('benefits', models.IntegerField(default=0)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payroll', to='financeApp.Employee')),
            ],
        ),
    ]