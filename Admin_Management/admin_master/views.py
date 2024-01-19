
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from admin_master.models import *
from django.shortcuts import get_object_or_404

from django.conf import settings

def adm_master_dept_manage(request):

    msg=""
    m=""

    if request.method == 'POST':
        dn = request.POST.get('dn', '').strip()
        dc = request.POST.get('dc', '').strip()

        if not dn or not dc:
            msg = "Both Department Name and Department Code are required."

        elif Departments.objects.filter(dpname=dn,dpcode=dc).exists():
            msg = "Department Name and Department Code already exists."


        elif Departments.objects.filter(dpname=dn).exists():
            msg = "Department Name already exists."

        elif Departments.objects.filter(dpcode=dc).exists():
            msg = "Department Code already exists."

        else:
            Departments.objects.create(dpname=dn, dpcode=dc,status=0)
            m = "Department added successfully."
            # return redirect('adm_master_dept_manage') 
        
    dpt = Departments.objects.all()
    return render(request, 'adm_master_dept_manage.html', {'danger': msg,'departments': dpt,'success':m})
    
    # else:
    #     return render(request, 'adm_master_dept_manage.html', {})
    
    
def datapick(request) :
     dept_id=request.GET['id'] 
     responsedata=Departments.objects.get(id=dept_id)
    
     serialized_data={
         'name':responsedata.dpname,
         'code':responsedata.dpcode,
         'status':1 if responsedata.status else 0,   
     }
     return JsonResponse(serialized_data)


def delete_department(request):
    d_id = request.GET.get('id')
    try:
        department = Departments.objects.get(id=d_id)
        department.delete()
        return JsonResponse({'success': 'Department deleted successfully'})
    except Departments.DoesNotExist:
        return JsonResponse({'error': 'Department not found'}, status=404)

def update_department(request):
    
    if request.method == 'GET':
        dept_id = request.GET.get('id')
        new_name = request.GET.get('new_name').strip()
        new_code = request.GET.get('new_code').strip()
        new_status = request.GET.get('new_status')

        
           
        try:
                department = Departments.objects.get(id=dept_id)
                if not new_name or not new_code:
                    return JsonResponse({'message':'both fields should not be empty'})
                elif Departments.objects.filter(dpname=new_name,dpcode=new_code).exclude(id=dept_id).exists():
                    return JsonResponse({'message':'both fields are already exist'})
                elif Departments.objects.filter(dpname=new_name).exclude(id=dept_id).exists():
                    return JsonResponse({'message':'department name already exist'})
                elif Departments.objects.filter(dpname=new_code).exclude(id=dept_id).exists():
                    return JsonResponse({'message':'department code already exist'})
            

               
                department.dpname = new_name
                department.dpcode = new_code
                department.status = new_status
                department.save()

                return JsonResponse({'success':'data updated successfully'})
            
        except Departments.DoesNotExist:
                return JsonResponse({'message':'department not found'},status=404)
         
    # else:
    #     return JsonResponse({'message':'department not added'})

    # # return JsonResponse({'message': 'Invalid request'})
  


def adm_master_designation_manage(request):
    msg=""
    m=""

    if request.method == 'POST':
        desn = request.POST.get('desn', '').strip()
        desc = request.POST.get('desc', '').strip()

        if not desn or not desc:
            msg = "Both Designation Name and  Designation Code are required."

        
        elif Designation.objects.filter(dname=desn,dcode=desc).exists():
            msg = "Designation Name and Designation Code already exists."

        elif Designation.objects.filter(dname=desn).exists():
            msg = "Designation Name already exists."

        elif Designation.objects.filter(dcode=desc).exists():
            msg = "Designation Code already exists."

        else:
            Designation.objects.create(dname=desn, dcode=desc)
            m = "Designation added successfully."
            # return redirect('adm_master_dept_manage') 
        
    designation = Designation.objects.all()
    return render(request, 'adm_master_designation_manage.html', {'danger': msg,'desig': designation ,'success':m})

def des_datapick(request) :
     desi_id=request.GET['id'] 
     responsedata=Designation.objects.get(id=desi_id)
    
     serialized_data={
         'desname':responsedata.dname,
         'descode':responsedata.dcode,
         'desstatus':1 if responsedata.status else 0,   
     }
     return JsonResponse(serialized_data)


def update_designation(request):
    
    if request.method == 'GET':
        dept_id = request.GET.get('id')
        desname = request.GET.get('desname').strip()
        descode = request.GET.get('descode').strip()
        desstatus = request.GET.get('desstatus')

        
        try:
                designation = Designation.objects.get(id=dept_id)
                if not desname or not descode:
                    return JsonResponse({'error':'both fields should not be empty'})
                elif Designation.objects.filter(dname=desname,dcode=descode).exclude(id=dept_id).exists():
                    return JsonResponse({'error':'both fields are already exist'})
                elif Designation.objects.filter(dname=desname).exclude(id=dept_id).exists():
                    return JsonResponse({'error':'designation name already exist'})
                elif Designation.objects.filter(dcode=descode).exclude(id=dept_id).exists():
                    return JsonResponse({'error':'designation code already exist'})
            

               
                designation.dname = desname
                designation.dcode = descode
                designation.status = desstatus
                designation.save()

                return JsonResponse({'success':'data updated successfully'})
            
        except Designation.DoesNotExist:
                return JsonResponse({'error':'designation not found'},status=404)
        
def delete_designation(request):
    d_id = request.GET.get('id')
    try:
        designation = Designation.objects.get(id=d_id)
        designation.delete()
        return JsonResponse({'success': 'Designation deleted successfully'})
    except Designation.DoesNotExist:
        return JsonResponse({'error': 'Designation not found'}, status=404)
         
    



def adm_master_qualification_manage(request):
    msg=""
    m=""

    if request.method == 'POST':
        qua_name = request.POST.get('qua_name', '').strip()

        if not qua_name :
            msg = "Qualification Name is required."

        
        elif Qualification.objects.filter(qname=qua_name).exists():
            msg = "Qualification Name is already exists."


        else:
            Qualification.objects.create(qname=qua_name)
            m = "Qualification added successfully."
            # return redirect('adm_master_dept_manage') 
        
    qualification = Qualification.objects.all()
    return render(request, 'adm_master_qualification_manage.html', {'danger': msg,'qualification': qualification ,'success':m})

def qua_datapick(request) :
     q_id=request.GET['id'] 
     responsedata=Qualification.objects.get(id=q_id)
    
     serialized_data={
         'qua_name':responsedata.qname,
         'qua_status':1 if responsedata.status else 0,   
     }
     return JsonResponse(serialized_data)

def update_qualification(request):
    
    if request.method == 'GET':
        q_id = request.GET.get('id')
        qua_name = request.GET.get('qua_name').strip()
        qua_status = request.GET.get('qua_status')

        
        try:
                qualification = Qualification.objects.get(id=q_id)
                if not qua_name :
                    return JsonResponse({'error':'please fill the field'})
                elif Qualification.objects.filter(qname=qua_name).exclude(id=q_id).exists():
                    return JsonResponse({'error':' Qualification is already exist'})

               
                qualification.qname = qua_name
                qualification.status = qua_status
                qualification.save()

                return JsonResponse({'success':'data updated successfully'})
            
        except Qualification.DoesNotExist:
                return JsonResponse({'error':'Qualification not found'},status=404)
        
        
def delete_qualification(request):
    q_id = request.GET.get('id')
    try:
        qualification = Qualification.objects.get(id=q_id)
        qualification.delete()
        return JsonResponse({'success': 'Qualification deleted successfully'})
    except Qualification.DoesNotExist:
        return JsonResponse({'error': 'Qualification not found'}, status=404)
         



def adm_master_class_manage(request):
    msg=""
    m=""

    if request.method == 'POST':
        class_name = request.POST.get('class_name', '').strip()

        if not class_name :
            msg = "Class Name is required."

        
        elif Class.objects.filter(cname=class_name).exists():
            msg = "Class Name is already exists."


        else:
            Class.objects.create(cname=class_name)
            m = "Class added successfully."
            # return redirect('adm_master_dept_manage') 
        
    cls = Class.objects.all()
    return render(request, 'adm_master_class_manage.html', {'danger': msg,'cls': cls ,'success':m})

def class_datapick(request) :
     c_id=request.GET['id'] 
     responsedata=Class.objects.get(id=c_id)
    
     serialized_data={
         'class_name':responsedata.cname,
         'class_status':1 if responsedata.status else 0,   
     }
     return JsonResponse(serialized_data)

def update_class(request):
    
    if request.method == 'GET':
        c_id = request.GET.get('id')
        class_name = request.GET.get('class_name').strip()
        class_status = request.GET.get('class_status')

        
        try:
                cls = Class.objects.get(id=c_id)
                if not class_name :
                    return JsonResponse({'error':'please fill the field'})
                elif Class.objects.filter(cname=class_name).exclude(id=c_id).exists():
                    return JsonResponse({'error':' Class is already exist'})

               
                cls.cname = class_name
                cls.status = class_status
                cls.save()

                return JsonResponse({'success':'data updated successfully'})
            
        except Class.DoesNotExist:
                return JsonResponse({'error':'Class not found'},status=404)
        
def delete_class(request):
    c_id = request.GET.get('id')
    try:
        cls = Class.objects.get(id=c_id)
        cls.delete()
        return JsonResponse({'success': 'Class deleted successfully'})
    except Qualification.DoesNotExist:
        return JsonResponse({'error': 'Class not found'}, status=404)


def adm_master_division_manage(request):
    msg=""
    m=""

    if request.method == 'POST':
        div_name = request.POST.get('div_name', '').strip()

        if not div_name :
            msg = "Division is required."

        
        elif Division.objects.filter(dname=div_name).exists():
            msg = "Division is already exists."


        else:
            Division.objects.create(dname=div_name)
            m = "division added successfully."
    division = Division.objects.all()
    return render(request, 'adm_master_division_manage.html', {'danger': msg,'division': division ,'success':m})

def div_datapick(request) :
     d_id=request.GET['id'] 
     responsedata=Division.objects.get(id=d_id)
    
     serialized_data={
         'div_name':responsedata.dname,
         'div_status':1 if responsedata.status else 0,   
     }
     return JsonResponse(serialized_data)

def update_division(request):
    
    if request.method == 'GET':
        d_id = request.GET.get('id')
        div_name = request.GET.get('div_name').strip()
        div_status = request.GET.get('div_status')

        
        try:
                div = Division.objects.get(id=d_id)
                if not div_name :
                    return JsonResponse({'error':'please fill the field'})
                elif Division.objects.filter(dname=div_name).exclude(id=d_id).exists():
                    return JsonResponse({'error':' Division is already exist'})

               
                div.dname = div_name
                div.status = div_status
                div.save()

                return JsonResponse({'success':'data updated successfully'})
            
        except Division.DoesNotExist:
                return JsonResponse({'error':'Division not found'},status=404)

def delete_division(request):
    d_id = request.GET.get('id')
    try:
        div = Division.objects.get(id=d_id)
        div.delete()
        return JsonResponse({'success': 'Division deleted successfully'})
    except Division.DoesNotExist:
        return JsonResponse({'error': 'Division  not found'}, status=404)

        



           
def adm_master_emp_cat_manage(request):
    msg=""
    m=""

    if request.method == 'POST':
        emp_cat = request.POST.get('emp_cat', '').strip()
        emp_area = request.POST.get('emp_area', '').strip()

        if not emp_cat or not emp_area:
            msg = "  Both Employee Category Name and Employee Category Area are required."

        
        elif Employee_Category.objects.filter(ename=emp_cat).exists():
            msg = "Employee Category Name already exists."

       
        else:
            Employee_Category.objects.create(ename=emp_cat, area=emp_area)
            m = "Employee Category added successfully."
            # return redirect('adm_master_dept_manage') 
        
    emp_cat_details = Employee_Category.objects.all()
    return render(request, 'adm_master_emp_cat_manage.html', {'settings':settings,'danger': msg,'emp_cat_details':emp_cat_details ,'success':m})

def emp_datapick(request) :
     emp_id=request.GET['id'] 
     responsedata=Employee_Category.objects.get(id=emp_id)
    
     serialized_data={
         'emp_cat_name':responsedata.ename,
         'emp_cat_area':responsedata.area,
         'emp_status':1 if responsedata.status else 0,   
     }
     return JsonResponse(serialized_data)


def update_emp_cat(request):
    
    if request.method == 'GET':
        e_id = request.GET['id']
        emp_name = request.GET['emp_name'].strip()
        emp_area = request.GET['emp_area'].strip()
        emp_status = request.GET['emp_status']

        
        try:
                emp_details = Employee_Category.objects.get(id=e_id)
                if not emp_name or not emp_area :
                    return JsonResponse({'error':'both fields should not be empty'})
                elif Employee_Category.objects.filter(ename=emp_name).exclude(id=e_id).exists():
                    return JsonResponse({'error':'Employee Category Name already exist'})
               
                emp_details.ename = emp_name
                emp_details.area = emp_area
                emp_details.status = emp_status
                emp_details.save()

                return JsonResponse({'success':'data updated successfully'})
            
        except Employee_Category.DoesNotExist:
                return JsonResponse({'error':'Employee Category not found'},status=404)
       

def delete_emp_cat(request):
    e_id = request.GET.get('id')
    try:
        emp_details = Employee_Category.objects.get(id=e_id)
        emp_details.delete()
        return JsonResponse({'success': 'Employee Category deleted successfully'})
    except Designation.DoesNotExist:
        return JsonResponse({'error': 'Employee Category not found'}, status=404)
    
def adm_master_subject(request):
    msg=""
    m=""
    class_details=Class.objects.filter(status=1)

    if request.method == 'POST':
        sub_name = request.POST.get('sub_name', '').strip()
       

        if not sub_name :
            msg = "Subject Name is required."

        
        elif Subject.objects.filter(subject_name=sub_name).exists():
            msg = "Subject Name is already exists."


        else:
            checkvalue=request.POST.getlist("checkid")
            if checkvalue: 
                subobj,create=Subject.objects.get_or_create(subject_name=sub_name)
            for chkid in checkvalue:
                 classins=get_object_or_404(Class,pk=(chkid))
                 objins=SubjectClass(subject_id=subobj,class_id=classins)
                 objins.save()

            m = "Subject added successfully."
    sub_details = Subject.objects.all()
    return render(request,'adm_master_subject.html',{'class':class_details,'danger': msg,'success':m,'sub_details':sub_details})




def sub_datapick(request):
    try:
        sub_id = request.GET.get('id')
        # class_ins = request.GET.get('c_id')
        
        # Retrieve subject details
        subject_data = Subject.objects.get(id=sub_id)
        
        # Retrieve associated classes for the subject
        class_data = SubjectClass.objects.filter(subject_id=sub_id).values_list('class_id__cname', flat=True)
        
        serialized_data = {
            'sub_name': subject_data.subject_name,
            'sub_status': 1 if subject_data.status else 0,
            'class_details': list(class_data),
        }
        
        return JsonResponse(serialized_data)
    
    except Subject.DoesNotExist:
        return JsonResponse({'error': 'Subject not found'}, status=404)
    except SubjectClass.DoesNotExist:
        return JsonResponse({'error': 'Class not found'}, status=404)


# def update_emp_cat(request):
    
#     if request.method == 'GET':
#         s_id = request.GET['id']
#         sub_name = request.GET['sub_name'].strip()
#         sub_class = request.GET['sub_class'].strip()
#         sub_status = request.GET['sub_status']

        
#         try:
#                 sub_details = Subject.objects.get(id=s_id)
#                 class_data = SubjectClass.objects.filter(subject_id=s_id).values_list('class_id__cname', flat=True)
        
#                 if not sub_name or not sub_class:
#                     msg = "Subject Name and Class is required."

        
#                 elif Subject.objects.filter(subject_name=sub_name).exclude(id=s_id).exists():
#                     msg = "Subject Name is already exists."
#                 # elif SubjectClass.objects.filter(class_id=sub_class).exclude(id=s_id).exists():
#                 #     msg = "Subject Name is already exists."
#                 checkvalue=request.POST.getlist("checkid")
#                 if checkvalue: 
#                     subobj,create=Subject.objects.get_or_create(subject_name=sub_name)
#                 for chkid in checkvalue:
#                     classins=get_object_or_404(Class,pk=(chkid))
#                     objins=SubjectClass(subject_id=subobj,class_id=classins)
#                     objins.save()    

               
#                 sub_details.subject_name = sub_name
#                 class_data.class_id = sub_class
#                 sub_details.status = sub_status
#                 sub_details.save()

#                 return JsonResponse({'success':'data updated successfully'})
            
#         except Employee_Category.DoesNotExist:
#                 return JsonResponse({'error':msg},status=404)
       




# def update_subject(request):
#     if request.method == 'GET':
#         s_id = request.GET.get('id')
#         sub_name = request.GET.get('sub_name').strip()
#         sub_class = request.GET.get('sub_class').strip()
#         sub_status = request.GET.get('sub_status')

#         try:
#             sub_details = Subject.objects.get(id=s_id)
#             class_data = SubjectClass.objects.filter(subject_id=s_id,)
            
#             if not sub_name or not sub_class:
#                 return JsonResponse({'error': "Subject Name and Class are required."}, status=400)
            
#             elif Subject.objects.filter(subject_name=sub_name).exclude(id=s_id).exists():
#                 return JsonResponse({'error': "Subject Name already exists."}, status=400)
            
#             sub_details.subject_name = sub_name
#             sub_details.status = sub_status
#             sub_details.save()

#             # Clear existing subject classes
#             class_data.delete()

#             checkvalue = request.GET.getlist("checkid")
#             if checkvalue: 
#                 subobj, _ = Subject.objects.get_or_create(subject_name=sub_name)
#                 for chkid in checkvalue:
#                     classins = get_object_or_404(Class, pk=chkid)
#                     objins = SubjectClass(subject_id=subobj, class_id=classins)
#                     objins.save()

#             return JsonResponse({'success': 'Data updated successfully'})

#         except Subject.DoesNotExist:
#             return JsonResponse({'error': 'Subject not found'}, status=404)
#         except Class.DoesNotExist:
#             return JsonResponse({'error': 'Class not found'}, status=404)



