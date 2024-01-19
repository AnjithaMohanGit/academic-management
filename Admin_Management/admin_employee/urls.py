from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('adm_emp_manage/', views.adm_emp_manage,name='adm_emp_manage'),
    path('get_subjects/', views.get_subjects, name='get_subjects'),
    path('adm_emp_table/', views.adm_emp_table, name='adm_emp_table'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)