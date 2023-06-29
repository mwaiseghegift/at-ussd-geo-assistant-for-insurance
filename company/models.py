from django.db import models
# pointfied for geolocation
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.contrib.gis.db.models.functions import Distance as DistanceFunc
import uuid
from accounts.models import User, Doctor

# Create your models here.

class InsuranceCompany(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'insurance_company'
        verbose_name_plural = 'insurance companies'

class InsuranceHospital(models.Model):
    name = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    location = gis_models.PointField()
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        db_table = 'insurance_hospital'

    def __str__(self):
        return self.address
    
    def get_distance(self, lat, lng):
        user_location = Point(lng, lat, srid=4326)
        return self.location.distance(user_location) * Distance(m=1)
    
    def get_distance_in_km(self, lat, lng):
        return self.get_distance(lat, lng).km
    

class InsuranceCustomer(models.Model):
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'insurance_customer'
        verbose_name_plural = 'insurance customers'
    

class InsuranceClaim(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    hospital = models.ForeignKey(InsuranceHospital, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.description
    
    class Meta:
        ordering = ['-date_created']
        db_table = 'insurance_claim'
        verbose_name_plural = 'insurance claims'

class Policy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    coverage = models.TextField()
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    # Add other fields related to the policy

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'policy'
        verbose_name_plural = 'policies'

