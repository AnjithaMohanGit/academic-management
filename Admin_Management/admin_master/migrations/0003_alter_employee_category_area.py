# Generated by Django 5.0 on 2024-01-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_master', '0002_departments_delete_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_category',
            name='area',
            field=models.IntegerField(choices=[(1, 'Accountant'), (2, 'Cafeteria'), (3, 'Librarian'), (4, 'Teacher'), (5, 'Others')]),
        ),
    ]
