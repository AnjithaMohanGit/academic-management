from django.urls import path
from . import views

urlpatterns = [
    path('adm_master_dept_manage/', views.adm_master_dept_manage,name='adm_master_dept_manage'),
    path('editdept_manage/', views.datapick,name='data_pick'),
    path('update_department/', views.update_department, name='update_department'),
    path('dltdept_manage/', views.delete_department, name='delete_department'),

    path('adm_master_designation_manage/', views.adm_master_designation_manage,name='adm_master_designation_manage'),
    path('editdesi_manage/', views.des_datapick,name='des_data_pick'),
    path('update_designation/',views.update_designation,name="update_designation"),
    path('delete_designation/',views.delete_designation,name="delete_designation"),
    
    path('adm_master_qualification_manage/', views.adm_master_qualification_manage,name='adm_master_qualification_manage'),
    path('edit_qualification/', views.qua_datapick,name='qua_data_pick'),
    path('update_qualification/',views.update_qualification,name="update_qualification"),
    path('delete_qualification/',views.delete_qualification,name="delete_qualification"),
    
    path('adm_master_class_manage/', views.adm_master_class_manage,name='adm_master_class_manage'),
    path('edit_class/', views.class_datapick,name='class_data_pick'),
    path('update_class/',views.update_class,name="update_class"),
    path('delete_class/',views.delete_class,name="delete_class"),
    
    path('adm_master_division_manage/', views.adm_master_division_manage,name='adm_master_division_manage'),
    path('edit_division/', views.div_datapick,name='div_data_pick'),
    path('update_division/',views.update_division,name="update_division"),
    path('delete_division/',views.delete_division,name="delete_division"),
    
    path('adm_master_emp_cat_manage/', views.adm_master_emp_cat_manage,name='adm_master_emp_cat_manage'),
    path('edit_emp_cat/', views.emp_datapick,name='emp_data_pick'),
    path('update_emp_cat/',views.update_emp_cat,name="update_emp_cat"),
    path('delete_emp_cat/',views.delete_emp_cat,name="delete_emp_cat"),

    path('adm_master_subject/',views.adm_master_subject,name="adm_master_subject"),
    path('edit_subject/', views.sub_datapick,name='sub_data_pick'),
    # path('update_subject/',views.update_subject,name="update_subject"),
    # path('delete_subject/',views.delete_subject,name="delete_subject"),

] 
