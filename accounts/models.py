from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20)
    is_insurance_company = models.BooleanField(default=False)
    is_hospital = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=100, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    class Meta:
        db_table = 'user'


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=(
        ('Male', "Male"),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'doctor'
        
    