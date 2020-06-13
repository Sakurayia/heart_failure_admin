"""heart_failure_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views as api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', api.login),
    path('fetch_patients', api.fetch_patients),
    path('fetch_admission_info', api.fetch_admission_info),
    path('fetch_lab_info', api.fetch_lab_info),
    path('fetch_cpt_info', api.fetch_cpt_info),
    path('fetch_caregiver_patients', api.fetch_caregiver_patients),
    path('fetch_prescription', api.fetch_prescription),
    path('modify_patient', api.modify_patient),
    path('modify_admission', api.modify_admission),
    path('add_patient', api.add_patient),
    path('add_admission', api.add_admission),
    path('delete_patient', api.delete_patient),
    path('delete_admission', api.delete_admission),
    path('fetch_home_statistic', api.fetch_home_statistic),
    path('fetch_month_patient', api.fetch_month_patient),
    path('fetch_caregiver', api.fetch_caregiver),
    path('modify_caregiver', api.modify_caregiver),
    path('add_caregiver', api.add_caregiver),
    path('delete_caregiver', api.delete_caregiver),
    path('fetch_user', api.fetch_user),
    path('update_user', api.update_user),
]
