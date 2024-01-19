
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from admin_master.models import *
from admin_employee.models import *
from django.conf import settings
from django.db import transaction
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
import qrcode
from io import BytesIO
import os
from django.conf import settings

def generate_qr_code(emp_name, department, status):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    data = f"Employee Name: {emp_name}\nDepartment: {department}\nStatus: {'Active' if status else 'Inactive'}"
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a BytesIO buffer
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)

    # Get the media root path
    media_root = settings.MEDIA_ROOT

    # Create the barcode directory if not exists
    barcode_dir = os.path.join(media_root, 'baArcode')
    os.makedirs(barcode_dir, exist_ok=True)

    # Define the path to save the QR code
    qr_code_path = os.path.join(barcode_dir, f'qrcode_{emp_name}.png')

    # Save the image to the specified path
    img.save(qr_code_path)

    # Convert the saved image to an InMemoryUploadedFile
    qr_code_image = InMemoryUploadedFile(
        ContentFile(buffer.read()),
        None,
        os.path.basename(qr_code_path),
        'image/png',
        buffer.tell(),
        None
    )

    return qr_code_image



def adm_emp_manage(request):
    
    if request.POST:
        
        a=request.POST['name']
        b=request.FILES['emp_photo']
        c=request.POST['phone']
        d=request.POST['dob']
        e=request.POST['address']
        f=request.POST['dpt_status']
        depid=Departments.objects.get(id=f)
        g=request.POST['des_status']
        desid=Designation.objects.get(id=g)
        h=request.POST['qua_status']
        quaid=Qualification.objects.get(id=h)
        k=request.POST['emp_status']
        emp_array=k.split("+")
        empid=Employee_Category.objects.get(id=emp_array[0])
        l=request.POST['salary']
        m=request.POST['joindate']
        n=request.POST['mail']
        o=request.POST['gender']

        new_employee, createemp = Employee.objects.get_or_create(emp_name=a,photo=b,dob=d,gender=o,address=e,email=n,emp_phone=c,emp_cat_id=empid,qualification_id=quaid,department_id=depid,designation_id=desid,salary_id=l,joinday=m)
        
        qr_code_image = generate_qr_code(a, depid.dpname, new_employee.status)

    # Save the generated QR code to the employee instance
        new_employee.barcode = qr_code_image
        new_employee.save()

        # Handle department_employee details
        
        dept_emp_obj = department_employee(dept_id=depid, emp_id=new_employee, from_date=m)
        dept_emp_obj.save()

        # Handle designation_employee details
        
        desig_emp_obj = designation_employee(des_id=desid, emp_id=new_employee, from_date=m)
        desig_emp_obj.save()


        salary_emp_obj = Salary(salary_id=l, emp_id=new_employee, from_date=m)
        salary_emp_obj.save()


        class_ids = request.POST.getlist('classids')
        division_ids = request.POST.getlist('divisionids')
        subject_ids = request.POST.getlist('subjectids')

        try:
            with transaction.atomic():
                for class_id, division_id, subject_id in zip(class_ids, division_ids, subject_ids):
                    class_instance = Class.objects.get(id=class_id)
                    division_instance = Division.objects.get(id=division_id)
                    subject_instance = Subject.objects.get(id=subject_id)

                    sub_cls_div_obj = sub_cls_div(
                        emp_id=new_employee,
                        cls_id=class_instance,
                        div_id=division_instance,
                        sub_id=subject_instance
                    )
                    sub_cls_div_obj.save()

        except Exception as e:
            # Handle exceptions if any during the creation of sub_cls_div instances
            print(e)
        
       
        

    qualification=Qualification.objects.order_by('qname').filter(status=1)
    department=Departments.objects.order_by('dpname').filter(status=1)
    designation=Designation.objects.order_by('dname').filter(status=1)
    class_details=Class.objects.order_by('cname').filter(status=1)
    division=Division.objects.order_by('dname').filter(status=1)
    subject=Subject.objects.order_by('subject_name').filter(status=1)
    emp_catogory=Employee_Category.objects.order_by('ename').filter(status=1)
    return render(request, 'adm_emp_add.html',{'qualification': qualification,'department':department,'designation':designation,'emp_catogory': emp_catogory,'class_details':class_details,'division':division,'subject':subject})


def get_subjects(request):
    class_id = request.GET.get('class_id')
    subjects = SubjectClass.objects.filter(class_id=class_id).values('subject_id__id', 'subject_id__subject_name')
    subjects_dict = {subject['subject_id__id']: subject['subject_id__subject_name'] for subject in subjects}
    return JsonResponse(subjects_dict)

def adm_emp_table(request):
    l=Employee.objects.all()
    return render(request,'adm_emp_table.html',{'employee':l})


  