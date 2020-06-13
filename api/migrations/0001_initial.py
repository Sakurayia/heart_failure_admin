# Generated by Django 3.0.4 on 2020-04-10 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admissions',
            fields=[
                ('row_id', models.IntegerField()),
                ('subject_id', models.IntegerField()),
                ('hadm_id', models.IntegerField(primary_key=True, serialize=False)),
                ('admittime', models.DateTimeField()),
                ('dischtime', models.DateTimeField()),
                ('deathtime', models.DateTimeField(blank=True, null=True)),
                ('admission_type', models.CharField(max_length=50)),
                ('admission_location', models.CharField(max_length=50)),
                ('discharge_location', models.CharField(max_length=50)),
                ('insurance', models.CharField(max_length=255)),
                ('language', models.CharField(blank=True, max_length=10, null=True)),
                ('religion', models.CharField(blank=True, max_length=50, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=50, null=True)),
                ('ethnicity', models.CharField(blank=True, max_length=200, null=True)),
                ('edregtime', models.DateTimeField(blank=True, null=True)),
                ('edouttime', models.DateTimeField(blank=True, null=True)),
                ('diagnosis', models.CharField(max_length=300)),
                ('hospital_expire_flag', models.IntegerField()),
                ('has_chartevents_data', models.IntegerField()),
            ],
            options={
                'db_table': 'admissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Caregiver',
            fields=[
                ('row_id', models.IntegerField()),
                ('cgid', models.IntegerField(primary_key=True, serialize=False)),
                ('label', models.CharField(blank=True, max_length=15, null=True)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'caregiver',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cpt',
            fields=[
                ('row_id', models.IntegerField(primary_key=True, serialize=False)),
                ('costcenter', models.CharField(max_length=10)),
                ('chartdate', models.CharField(blank=True, max_length=50, null=True)),
                ('cpt_cd', models.CharField(max_length=10)),
                ('cpt_number', models.IntegerField()),
                ('cpt_suffix', models.CharField(blank=True, max_length=5, null=True)),
                ('ticket_id_seq', models.IntegerField(blank=True, null=True)),
                ('sectionheader', models.CharField(max_length=50)),
                ('subsectionheader', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'cpt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Datetimeevents',
            fields=[
                ('row_id', models.IntegerField(primary_key=True, serialize=False)),
                ('icustay_id', models.IntegerField(blank=True, null=True)),
                ('itemid', models.IntegerField()),
                ('charttime', models.DateTimeField()),
                ('storetime', models.DateTimeField()),
                ('value', models.DateTimeField(blank=True, null=True)),
                ('valueuom', models.CharField(max_length=50)),
                ('warning', models.SmallIntegerField(blank=True, null=True)),
                ('error', models.SmallIntegerField(blank=True, null=True)),
                ('resultstatus', models.CharField(blank=True, max_length=50, null=True)),
                ('stopped', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'datetimeevents',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DCpt',
            fields=[
                ('row_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.SmallIntegerField()),
                ('sectionrange', models.CharField(max_length=100)),
                ('sectionheader', models.CharField(max_length=50)),
                ('subsectionrange', models.CharField(max_length=100)),
                ('subsectionheader', models.CharField(max_length=300)),
                ('codesuffix', models.CharField(blank=True, max_length=5, null=True)),
                ('mincodeinsubsection', models.IntegerField()),
                ('maxcodeinsubsection', models.IntegerField()),
            ],
            options={
                'db_table': 'd_cpt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DLabitems',
            fields=[
                ('row_id', models.IntegerField()),
                ('itemid', models.IntegerField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=100)),
                ('fluid', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('loinc_code', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'd_labitems',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Labevents',
            fields=[
                ('row_id', models.IntegerField(primary_key=True, serialize=False)),
                ('charttime', models.DateTimeField()),
                ('value', models.CharField(blank=True, max_length=200, null=True)),
                ('valuenum', models.FloatField(blank=True, null=True)),
                ('valueuom', models.CharField(blank=True, max_length=20, null=True)),
                ('flag', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'labevents',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('row_id', models.IntegerField()),
                ('subject_id', models.IntegerField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=5)),
                ('dob', models.DateTimeField()),
                ('dod', models.DateTimeField(blank=True, null=True)),
                ('dod_hosp', models.DateTimeField(blank=True, null=True)),
                ('dod_ssn', models.DateTimeField(blank=True, null=True)),
                ('expire_flag', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'patients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PatientsInfo',
            fields=[
                ('subject_id', models.IntegerField()),
                ('hadm_id', models.IntegerField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=5)),
                ('age', models.IntegerField()),
                ('insurance', models.CharField(max_length=255)),
                ('language', models.CharField(blank=True, max_length=10, null=True)),
                ('religion', models.CharField(blank=True, max_length=50, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=50, null=True)),
                ('ethnicity', models.CharField(blank=True, max_length=200, null=True)),
                ('expire_flag', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'patients_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('row_id', models.IntegerField(primary_key=True, serialize=False)),
                ('icustay_id', models.IntegerField(blank=True, null=True)),
                ('startdate', models.DateTimeField(blank=True, null=True)),
                ('enddate', models.DateTimeField(blank=True, null=True)),
                ('drug_type', models.CharField(max_length=100)),
                ('drug', models.CharField(max_length=100)),
                ('drug_name_poe', models.CharField(blank=True, max_length=100, null=True)),
                ('drug_name_generic', models.CharField(blank=True, max_length=100, null=True)),
                ('formulary_drug_cd', models.CharField(blank=True, max_length=120, null=True)),
                ('gsn', models.CharField(blank=True, max_length=200, null=True)),
                ('ndc', models.CharField(blank=True, max_length=120, null=True)),
                ('prod_strength', models.CharField(blank=True, max_length=120, null=True)),
                ('dose_val_rx', models.CharField(blank=True, max_length=120, null=True)),
                ('dose_unit_rx', models.CharField(blank=True, max_length=120, null=True)),
                ('form_val_disp', models.CharField(blank=True, max_length=120, null=True)),
                ('form_unit_disp', models.CharField(blank=True, max_length=120, null=True)),
                ('route', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'prescription',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]