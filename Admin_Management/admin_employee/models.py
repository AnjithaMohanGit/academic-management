from django.db import models
from admin_master.models import Departments,Designation,Qualification,Class,Division,Subject,Employee_Category

# Create your models here.
class Employee (models.Model):
    emp_name= models.CharField(max_length=100)
    dob=models.DateField()
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    emp_phone= models.IntegerField()
    department_id= models.ForeignKey(Departments,on_delete=models.CASCADE)
    designation_id= models.ForeignKey(Designation,on_delete=models.CASCADE)
    qualification_id= models.ForeignKey(Qualification,on_delete=models.CASCADE)
    emp_cat_id= models.ForeignKey(Employee_Category,on_delete=models.CASCADE)
    salary_id= models.DecimalField(max_digits=10,decimal_places=2)
    joinday=models.DateField()
    photo= models.ImageField(upload_to="Images/", blank=True,null=True) 
    barcode= models.ImageField(upload_to="barcode/",blank=True,null=True) 
    status=models.BooleanField(default=True)

    EMPLOYEE_GENDER=[
        (0,'Male'),
        (1,'Female'),
        (2,'Others'),
    ] 
    gender= models.IntegerField(choices=EMPLOYEE_GENDER)

class sub_cls_div(models.Model):
    emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    cls_id=models.ForeignKey(Class,on_delete=models.CASCADE)
    div_id=models.ForeignKey(Division,on_delete=models.CASCADE)
    sub_id=models.ForeignKey(Subject,on_delete=models.CASCADE)

class department_employee(models.Model):
    dept_id=models.ForeignKey(Departments,on_delete=models.CASCADE)
    emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    from_date=models.DateField()
    to_date=models.DateField(null=True, blank=True)

class designation_employee(models.Model):
    des_id=models.ForeignKey(Designation,on_delete=models.CASCADE)
    emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    from_date=models.DateField()
    to_date=models.DateField(null=True, blank=True)

class Salary(models.Model):
    salary_id= models.DecimalField(max_digits=10,decimal_places=2)
    emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    from_date=models.DateField()
    to_date=models.DateField(null=True, blank=True)

    