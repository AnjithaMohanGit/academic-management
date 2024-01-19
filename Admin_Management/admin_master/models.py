from django.db import models


class Qualification (models.Model):
    qname= models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    
class Designation (models.Model):
    dname= models.CharField(max_length=100)
    dcode= models.CharField(max_length=50)
    status=models.BooleanField(default=True)

class Class (models.Model):
    cname= models.CharField(max_length=100)
    status=models.BooleanField(default=True)

class Division (models.Model):
    dname= models.CharField(max_length=100)
    status=models.BooleanField(default=True)

class Departments (models.Model):
    dpname= models.CharField(max_length=100)
    dpcode= models.CharField(max_length=50)
    status=models.BooleanField(default=True)


class Employee_Category (models.Model):
    EMPLOYEE_CATEGORY_AREA=[
        (1,'Accountant'),
        (2,'Cafeteria'),
        (3,'Librarian'),
        (4,'Teacher'),
        (5,'Others'),
    ]

    ename= models.CharField(max_length=100)
    area= models.IntegerField(choices=EMPLOYEE_CATEGORY_AREA)
    status=models.BooleanField(default=True)

class Subject (models.Model):
    subject_name= models.CharField(max_length=100)
    status=models.BooleanField(default=True)


class SubjectClass (models.Model):
    subject_id= models.ForeignKey("Subject",on_delete=models.CASCADE)
    class_id=models.ForeignKey("Class",on_delete=models.CASCADE)








# Create your models here.
