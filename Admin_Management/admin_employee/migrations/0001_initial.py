# Generated by Django 5.0 on 2024-01-15 05:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_master', '0005_subjectclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('emp_phone', models.IntegerField()),
                ('salary_id', models.DecimalField(decimal_places=2, max_digits=10)),
                ('joinday', models.DateField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Images/')),
                ('barcode', models.ImageField(blank=True, null=True, upload_to='barcode/')),
                ('status', models.BooleanField(default=True)),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Others')])),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_master.departments')),
                ('designation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_master.designation')),
                ('emp_cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_master.employee_category')),
                ('qualification_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_master.qualification')),
            ],
        ),
        migrations.CreateModel(
            name='designation_employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('des_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_master.designation')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='department_employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_master.departments')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_id', models.DecimalField(decimal_places=2, max_digits=10)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='sub_cls_div',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cls_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_master.class')),
                ('div_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_master.division')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_employee.employee')),
                ('sub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_master.subject')),
            ],
        ),
    ]
