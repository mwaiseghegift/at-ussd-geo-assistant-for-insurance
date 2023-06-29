from atexit import register
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Doctor
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_admin', 'is_hospital','is_customer')
    search_fields = ( 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_admin','is_customer','is_hospital')
    ordering = ('email',)

    fieldsets = (
        (None, {
            "fields": (
                'email',
                'first_name',
                'last_name',
                'password',
                'phone_no',
            ), 
        }),
        ('Status', {
            "fields": (
                'is_active',
            ), 
        }),
        ("Permissions", {
            "fields": (
                'is_superuser',
                'is_admin', 

            ), 
        }),
        ("Special Permissions", {
            "fields": (
                'user_permissions',
            ), 
        }),
    )
admin.site.register(Doctor)