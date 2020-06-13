from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Max
from api import models
from api import util
import json
import datetime


def login(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    res = dict()
    try:
        user = models.User.objects.get(username=username, password=password)
        res['status'] = 200
        res['authority'] = user.authority
    except models.User.DoesNotExist:
        res['status'] = 400
    return JsonResponse(res, safe=False)


def fetch_patients(request):
    data = json.loads(request.body)
    res = dict()
    try:
        patients = models.PatientsInfo.objects
        if('subject_id' in data and len(data['subject_id']) > 0):
            patients = patients.filter(subject_id=data['subject_id'])
        if('name' in data and len(data['name']) > 0):
            patients = patients.filter(name__contains=data['name'])
        if('gender' in data and len(data['gender']) > 0):
            patients = patients.filter(gender=data['gender'])
        if('age' in data and len(data['age']) > 0):
            patients = patients.filter(age=data['age'])
        if('language' in data and len(data['language']) > 0):
            patients = patients.filter(language__contains=data['language'])
        if('religion' in data and len(data['religion']) > 0):
            patients = patients.filter(religion__contains=data['religion'])
        if('marital_status' in data and len(data['marital_status']) > 0):
            patients = patients.filter(marital_status__contains=data['marital_status'])
        if('ethnicity' in data and len(data['ethnicity']) > 0):
            patients = patients.filter(ethnicity__contains=data['ethnicity'])
        if('expire_flag' in data and len(data['expire_flag']) > 0):
            patients = patients.filter(expire_flag=data['expire_flag'])
        res['status'] = 200
        res['data'] = list(patients.values())
    except Exception as e:
        res['status'] = 400
        res['err'] = str(e)
    return JsonResponse(res, safe=False)


def fetch_admission_info(request):
    data = json.loads(request.body)
    id = data['subject_id']
    res = dict()
    try:
        admissions = models.Admissions.objects.filter(subject_id=id).values("subject_id", "hadm_id", "admittime", "dischtime", "deathtime", "admission_type", "admission_location", "discharge_location", "insurance", "edregtime", "edouttime", "diagnosis", "hospital_expire_flag")
        res['status'] = 200
        adm_list = list(admissions)
        for item in adm_list:
            item['stay_days'] = (item['dischtime'] - item['admittime']).days
        res['admissions'] = adm_list
    except Exception as e:
        res['status'] = 400
        res['err'] = str(e)
    return JsonResponse(res, safe=False)


def fetch_lab_info(request):
    data = json.loads(request.body)
    id = data['hadm_id']
    res = dict()
    lab_list = list()
    for item in id:
        try:
            labevents = models.Labevents.objects.filter(hadm_id=item).values("hadm_id", "itemid", "itemid__label", "value", "valuenum", "valueuom", "itemid__fluid", "itemid__category", "flag", "charttime")
            res['status'] = 200
            lab_list.append(list(labevents))
            res['lab'] = lab_list
        except Exception as e:
            res['status'] = 400
            res['err'] = str(e)
    return JsonResponse(res, safe=False)


def fetch_cpt_info(request):
    data = json.loads(request.body)
    id = data['hadm_id']
    res = dict()
    cpt_list = list()
    for item in id:
        try:
            cpt = models.Cpt.objects.filter(hadm_id=item).values("row_id", "costcenter", "chartdate", "cpt_number", "ticket_id_seq", "sectionheader", "subsectionheader", "description").order_by('ticket_id_seq')
            res['status'] = 200
            cpt_list.append(list(cpt))
            res['cpt'] = cpt_list
        except Exception as e:
            res['status'] = 400
            res['err'] = str(e)
    return JsonResponse(res, safe=False)


def fetch_caregiver_patients(request):
    data = json.loads(request.body)
    cgid = data['cgid']
    res = dict()
    try:
        patients = models.CaregiverToPatients.objects.filter(cgid=cgid).values("subject_id", "label", "description").distinct()
        res['status'] = 200
        patients_list = list(patients)
        res['data'] = patients_list
    except Exception as e:
        res['status'] = 400
        res['err'] = str(e)
    return JsonResponse(res, safe=False)


def fetch_prescription(request):
    data = json.loads(request.body)
    id = data['hadm_id']
    res = dict()
    drug_list = list()
    for item in id:
        try:
            prescription = models.Prescription.objects.filter(hadm_id=item).values()
            res['status'] = 200
            prescription_list = list(prescription)
            for item in prescription_list:
                if(item['enddate'] is not None and item['startdate'] is not None):
                    item['days'] = (item['enddate'] - item['startdate']).days
                else:
                    item['days'] = -1
            drug_list.append(prescription_list)
            res['drug'] = drug_list
        except Exception as e:
            res['status'] = 400
            res['err'] = str(e)
    return JsonResponse(res, safe=False)


def modify_patient(request):
    data = json.loads(request.body)
    subject_id = data['subject_id']
    res = dict()
    try:
        patient = models.PatientsInfo.objects.filter(subject_id=subject_id)
        patient.update(name=data['name'], gender=data['gender'], age=data['age'], expire_flag=data['expire_flag'])
        patient.update(language=data['language'], religion=data['religion'], marital_status=data['marital_status'], ethnicity=data['ethnicity'])
        res['status'] = 200
    except Exception as e:
        res['status'] = 400
        res['err'] = str(e)
    return JsonResponse(res, safe=False)


def modify_admission(requset):
    data = json.loads(requset.body)
    hadm_id = data['hadm_id']
    res = dict()
    try:
        admission = models.Admissions.objects.filter(hadm_id=hadm_id)
        admittime = util.strToDatetime(data['admittime'])
        dischtime = util.strToDatetime(data['dischtime'])
        admission.update(admittime=admittime, dischtime=dischtime, admission_type=data['admission_type'], admission_location=data['admission_location'], discharge_location=data['discharge_location'], diagnosis=data['diagnosis'])
        if(data['deathtime'] is not None):
            deathtime = util.strToDatetime(data['deathtime'])
            admission.update(deathtime=deathtime)
            admission.update(hospital_expire_flag=1)
        else:
            admission.update(deathtime=None)
            admission.update(hospital_expire_flag=0)
        if(data['edregtime'] is not None):
            edregtime = util.strToDatetime(data['edregtime'])
            admission.update(edregtime=edregtime)
        else:
            admission.update(edregtime=None)
        if(data['edouttime'] is not None):
            edouttime = util.strToDatetime(data['edouttime'])
            admission.update(edouttime=edouttime)
        else:
            admission.update(edouttime=None)
        res['status'] = 200
    except Exception as e:
        res['status'] = 400
        res['err'] = str(e)
    return JsonResponse(res, safe=False)


def add_patient(request):
    data = json.loads(request.body)
    res = dict()
    try:
        subject_id = models.PatientsInfo.objects.all().aggregate(Max('subject_id'))
        new_subject_id = subject_id['subject_id__max'] + 1
        models.PatientsInfo.objects.create(
            subject_id=new_subject_id,
            name=data['name'],
            gender=data['gender'],
            age=data['age'],
            language=data['language'],
            religion=data['religion'],
            marital_status=data['marital_status'],
            ethnicity=data['ethnicity'],
            expire_flag=data['expire_flag']
        )
        res['status'] = 200
    except Exception as e:
        res['status'] = 400
        res['err'] = str(e)
    return JsonResponse(res, safe=False)


def add_admission(request):
    data = json.loads(request.body)
    res = dict()
    try:
        hadm_id = models.Admissions.objects.all().aggregate(Max('hadm_id'))
        new_hadm_id = hadm_id['hadm_id__max'] + 1
        models.Admissions.objects.create(
            subject_id=data['subject_id'],
            hadm_id=new_hadm_id,
            admittime=util.strToDatetime(data['admittime']),
            dischtime=util.strToDatetime(data['dischtime']),
            deathtime=util.strToDatetime(data['deathtime']) if data['deathtime'] is not None else None,
            admission_type=data['admission_type'],
            admission_location=data['admission_location'],
            discharge_location=data['discharge_location'],
            insurance=data['insurance'],
            language=data['language'],
            religion=data['religion'],
            marital_status=data['marital_status'],
            ethnicity=data['ethnicity'],
            edregtime=util.strToDatetime(data['edregtime']) if data['edregtime'] is not None else None,
            edouttime=util.strToDatetime(data['edouttime']) if data['edouttime'] is not None else None,
            diagnosis=data['diagnosis'],
            hospital_expire_flag = data['hospital_expire_flag'],
            has_chartevents_data = data['has_chartevents_data'],
        )
        admissions = models.Admissions.objects.filter(subject_id=data['subject_id']).values('hadm_id')
        res['status'] = 200
        res['hadm_id'] = list(admissions)
        res['new_hadm_id'] = new_hadm_id
    except Exception as e:
        res['status'] = 400
        res['err'] = str(e)
    return JsonResponse(res, safe=False)


def delete_patient(request):
    data = json.loads(request.body)
    subject_id = data['subject_id']
    res = dict()
    for item in subject_id:
        try:
            models.Prescription.objects.filter(subject_id=item).delete()
            models.Datetimeevents.objects.filter(subject_id=item).delete()
            models.Labevents.objects.filter(subject_id=item).delete()
            models.Cpt.objects.filter(subject_id=item).delete()
            models.Admissions.objects.filter(subject_id=item).delete()
            models.PatientsInfo.objects.filter(subject_id=item).delete()
            res['status'] = 200
        except Exception as e:
            res['status'] = 400
            res['err'] = str(e)
    return JsonResponse(res, safe=False)


def delete_admission(request):
    data = json.loads(request.body)
    hadm_id = data['hadm_id']
    res = dict()
    try:
        models.Datetimeevents.objects.filter(hadm_id=hadm_id).delete()
        models.Prescription.objects.filter(hadm_id=hadm_id).delete()
        models.Labevents.objects.filter(hadm_id=hadm_id).delete()
        models.Cpt.objects.filter(hadm_id=hadm_id).delete()
        models.Admissions.objects.filter(hadm_id=hadm_id).delete()
        res['status'] = 200
    except Exception as e:
        res['status'] = 400
        res['err'] = str(e)
    return JsonResponse(res, safe=False)


def fetch_home_statistic(request):
    res = dict()
    curr_time = datetime.datetime.now().date()
    end_year = 2120
    end_month = int(curr_time.strftime("%m"))
    end_day = int(curr_time.strftime("%d"))
    end_time = datetime.datetime(end_year, end_month, end_day)
    try:
        totalPatient = models.PatientsInfo.objects.all().count()
        healthyPatient = models.PatientsInfo.objects.filter(expire_flag=0).count()
        totalAdmission = models.Admissions.objects.all().count()
        totalCaregiver = models.Caregiver.objects.all().count()
        latestPatient = models.PatientsInfo.objects.all().order_by('-subject_id')[:6].values()
        latestAdmission = models.Admissions.objects.filter(dischtime__lte=end_time).order_by('-dischtime')[:6].values('row_id', 'subject_id', 'admittime', 'dischtime', 'deathtime', 'admission_type', 'admission_location', 'discharge_location', 'subject_id__name', 'subject__gender', 'subject__age', 'subject__language', 'subject__religion', 'subject__marital_status', 'subject__ethnicity', 'subject__expire_flag')
        latestCaregiver = models.Caregiver.objects.all().order_by('cgid')[:10].values()
        res['status'] = 200
        res['data'] = dict(totalPatient=totalPatient, healthyPatient=healthyPatient, totalAdmission=totalAdmission, totalCaregiver=totalCaregiver, latestPatient=list(latestPatient), latestAdmission=list(latestAdmission), latestCaregiver=list(latestCaregiver))
    except Exception as e:
        res['status'] = 400
        res['err'] = str(e)
    return JsonResponse(res, safe=False)


def fetch_month_patient(request):
    res = dict()
    months = list()
    for month in range(1, 13):
        try:
            number = models.Admissions.objects.filter(admittime__month=month).count()
            months.append(number)
            res['status'] = 200
            res['data'] = months
        except Exception as e:
            res['status'] = 400
            res['err'] = str(e)
    return JsonResponse(res, safe=False)


def fetch_caregiver(request):
    data = json.loads(request.body)
    res = dict()
    try:
        caregivers = models.Caregiver.objects
        if('cgid' in data and len(data['cgid']) > 0):
            caregivers = caregivers.filter(cgid=data['cgid'])
        if('name' in data and len(data['name']) > 0):
            caregivers = caregivers.filter(name__contains=data['name'])
        if('label' in data and len(data['label']) > 0):
            caregivers = caregivers.filter(label__contains=data['label'])
        if('description' in data and len(data['description']) > 0):
            caregivers = caregivers.filter(description__contains=data['description'])
        res['status'] = 200
        res['data'] = list(caregivers.values())
    except Exception as e:
        res['status'] = 400
        res['err'] = str(e)
    return JsonResponse(res, safe=False)


def modify_caregiver(request):
    data = json.loads(request.body)
    cgid = data['cgid']
    res = dict()
    try:
        caregiver = models.Caregiver.objects.filter(cgid=cgid)
        caregiver.update(name=data['name'], label=data['label'], description=data['description'])
        res['status'] = 200
    except Exception as e:
        res['status'] = 400
        res['err'] = str(e)
    return JsonResponse(res, safe=False)


def add_caregiver(request):
    data = json.loads(request.body)
    res = dict()
    try:
        cgid = models.Caregiver.objects.all().aggregate(Max('cgid'))
        new_cgid = cgid['cgid__max'] + 1
        models.Caregiver.objects.create(
            cgid=new_cgid,
            name=data['name'],
            label=data['label'],
            description=data['description']
        )
        res['status'] = 200
    except Exception as e:
        res['status'] = 400
        res['err'] = str(e)
    return JsonResponse(res, safe=False)


def delete_caregiver(request):
    data = json.loads(request.body)
    cgid = data['cgid']
    res = dict()
    for item in cgid:
        try:
            models.Datetimeevents.objects.filter(cgid=item).delete()
            models.Caregiver.objects.filter(cgid=item).delete()
            res['status'] = 200
        except Exception as e:
            res['status'] = 400
            res['err'] = str(e)
    return JsonResponse(res, safe=False)


def fetch_user(request):
    res = dict()
    try:
        users = models.User.objects.all().values()
        res['status'] = 200
        res['data'] = list(users)
    except Exception as e:
        res['status'] = 400
        res['err'] = str(e)
    return JsonResponse(res, safe=False)


def update_user(request):
    data = json.loads(request.body)
    add = data['add']
    update = data['update']
    delete = data['delete']
    res = dict()
    for item in update:
        try:
            user = models.User.objects.filter(row_id=item['row_id'])
            user.update(username=item['username'], password=item['password'], authority=item['authority'], status=item['status'], isDeletable=item['isDeletable'])
            res['status'] = 200
        except Exception as e:
            res['status'] = 400
            res['err'] = str(e)
    for item in add:
        try:
            models.User.objects.create(
                row_id=item['row_id'],
                username=item['username'],
                password=item['password'],
                authority=item['authority'],
                status=item['status'],
                isDeletable=item['isDeletable']
            )
            res['status'] = 200
        except Exception as e:
            res['status'] = 400
            res['err'] = str(e)
    for item in delete:
        try:
            models.User.objects.filter(row_id=item).delete()
            res['status'] = 200
        except Exception as e:
            res['status'] = 400
            res['err'] = str(e)
    return JsonResponse(res, safe=False)
