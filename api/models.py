# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admissions(models.Model):
    row_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey('PatientsInfo', models.DO_NOTHING, db_column='subject_id', to_field='subject_id')
    hadm_id = models.IntegerField()
    admittime = models.DateTimeField()
    dischtime = models.DateTimeField()
    deathtime = models.DateTimeField(blank=True, null=True)
    admission_type = models.CharField(max_length=50)
    admission_location = models.CharField(max_length=50)
    discharge_location = models.CharField(max_length=50)
    insurance = models.CharField(max_length=255)
    language = models.CharField(max_length=10, blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    marital_status = models.CharField(max_length=50, blank=True, null=True)
    ethnicity = models.CharField(max_length=200)
    edregtime = models.DateTimeField(blank=True, null=True)
    edouttime = models.DateTimeField(blank=True, null=True)
    diagnosis = models.CharField(max_length=300, blank=True, null=True)
    hospital_expire_flag = models.IntegerField(blank=True, null=True)
    has_chartevents_data = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admissions'


class Caregiver(models.Model):
    row_id = models.AutoField(primary_key=True)
    cgid = models.IntegerField()
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caregiver'


class Cpt(models.Model):
    row_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING)
    costcenter = models.CharField(max_length=10)
    chartdate = models.CharField(max_length=50, blank=True, null=True)
    cpt_cd = models.CharField(max_length=10)
    cpt_number = models.IntegerField(blank=True, null=True)
    cpt_suffix = models.CharField(max_length=5, blank=True, null=True)
    ticket_id_seq = models.IntegerField(blank=True, null=True)
    sectionheader = models.CharField(max_length=50, blank=True, null=True)
    subsectionheader = models.CharField(max_length=300, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cpt'


class DCpt(models.Model):
    row_id = models.AutoField(primary_key=True)
    category = models.SmallIntegerField()
    sectionrange = models.CharField(max_length=100)
    sectionheader = models.CharField(max_length=50)
    subsectionrange = models.CharField(max_length=100)
    subsectionheader = models.CharField(max_length=300)
    codesuffix = models.CharField(max_length=5, blank=True, null=True)
    mincodeinsubsection = models.IntegerField()
    maxcodeinsubsection = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_cpt'


class DLabitems(models.Model):
    row_id = models.AutoField(primary_key=True)
    itemid = models.IntegerField(unique=True)
    label = models.CharField(max_length=100)
    fluid = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    loinc_code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_labitems'


class Datetimeevents(models.Model):
    row_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING, blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField()
    charttime = models.DateTimeField()
    storetime = models.DateTimeField()
    cgid = models.ForeignKey(Caregiver, models.DO_NOTHING, db_column='cgid')
    value = models.DateTimeField(blank=True, null=True)
    valueuom = models.CharField(max_length=50)
    warning = models.SmallIntegerField(blank=True, null=True)
    error = models.SmallIntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datetimeevents'


class Labevents(models.Model):
    row_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING, blank=True, null=True)
    itemid = models.ForeignKey(DLabitems, models.DO_NOTHING, db_column='itemid', to_field='itemid')
    charttime = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=20, blank=True, null=True)
    flag = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labevents'


class Patients(models.Model):
    row_id = models.AutoField(primary_key=True)
    subject_id = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=5)
    dob = models.DateTimeField()
    dod = models.DateTimeField(blank=True, null=True)
    dod_hosp = models.DateTimeField(blank=True, null=True)
    dod_ssn = models.DateTimeField(blank=True, null=True)
    expire_flag = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'patients'


class Prescription(models.Model):
    row_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Patients, models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING)
    icustay_id = models.IntegerField(blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    drug_type = models.CharField(max_length=100)
    drug = models.CharField(max_length=100)
    drug_name_poe = models.CharField(max_length=100, blank=True, null=True)
    drug_name_generic = models.CharField(max_length=100, blank=True, null=True)
    formulary_drug_cd = models.CharField(max_length=120, blank=True, null=True)
    gsn = models.CharField(max_length=200, blank=True, null=True)
    ndc = models.CharField(max_length=120, blank=True, null=True)
    prod_strength = models.CharField(max_length=120, blank=True, null=True)
    dose_val_rx = models.CharField(max_length=120, blank=True, null=True)
    dose_unit_rx = models.CharField(max_length=120, blank=True, null=True)
    form_val_disp = models.CharField(max_length=120, blank=True, null=True)
    form_unit_disp = models.CharField(max_length=120, blank=True, null=True)
    route = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescription'


class User(models.Model):
    row_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    authority = models.CharField(max_length=30)
    status = models.IntegerField()
    isDeletable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class PatientsInfo(models.Model):
    row_id = models.AutoField(primary_key=True)
    subject_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=5)
    age = models.IntegerField()
    language = models.CharField(max_length=10, blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    marital_status = models.CharField(max_length=50, blank=True, null=True)
    ethnicity = models.CharField(max_length=200, blank=True, null=True)
    expire_flag = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'patients_new'


class CaregiverToPatients(models.Model):
    cgid = models.IntegerField()
    subject_id = models.IntegerField()
    label = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caregiver_to_patients'
