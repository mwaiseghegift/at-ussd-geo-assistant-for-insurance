# Generated by Django 4.2.1 on 2023-06-29 06:49

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'insurance_company',
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('coverage', models.TextField()),
                ('premium', models.DecimalField(decimal_places=2, max_digits=10)),
                ('insurance_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.insurancecompany')),
            ],
            options={
                'db_table': 'policy',
            },
        ),
        migrations.CreateModel(
            name='InsuranceHospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=20)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor')),
                ('insurance_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.insurancecompany')),
            ],
            options={
                'db_table': 'insurance_hospital',
            },
        ),
        migrations.CreateModel(
            name='InsuranceCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('insurance_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.insurancecompany')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'insurance_customer',
            },
        ),
        migrations.CreateModel(
            name='InsuranceClaim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.insurancehospital')),
                ('insurance_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.insurancecompany')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'insurance_claim',
                'ordering': ['-date_created'],
            },
        ),
    ]
