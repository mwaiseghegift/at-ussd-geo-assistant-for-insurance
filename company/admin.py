from django.contrib import admin
from .models import *
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.

@admin.register(InsuranceHospital)
class InsuranceHospitalAdmin(OSMGeoAdmin):
    list_display = ('name', 'address', 'contact_number', 'insurance_company', 'location')
    search_fields = ('name', 'address', 'contact_number', 'insurance_company__name')
    list_filter = ('insurance_company',)
    default_lon = 1.2921
    default_lat = 36.8219
    default_zoom = 10

@admin.register(InsuranceCompany)
class InsuranceCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number')
    search_fields = ('name', 'address', 'contact_number')

@admin.register(InsuranceClaim)
class InsuranceClaimAdmin(admin.ModelAdmin):
    list_display = ('user', 'insurance_company', 'hospital', 'description', 'amount', 'date_created')
    search_fields = ('user__username', 'insurance_company__name', 'hospital__name', 'description')
    list_filter = ('insurance_company',)

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'coverage', 'premium', 'insurance_company')
    search_fields = ('name', 'description', 'coverage', 'premium', 'insurance_company__name')
    list_filter = ('insurance_company',)

    