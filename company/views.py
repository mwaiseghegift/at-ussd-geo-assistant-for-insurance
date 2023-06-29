from django.shortcuts import render
from .models import InsuranceCompany, InsuranceHospital, InsuranceCustomer, InsuranceClaim
from decouple import config
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

# import package
import africastalking

# Initialize SDK
username = "alg-alchemists-insure"    # use 'sandbox' for development in the test environment
api_key = config('AFRICASTALKING_API_KEY')      # use your sandbox app API key for development in the test environment

africastalking.initialize(username, api_key)

# Initialize a service i.e SMS, USSD
sms = africastalking.SMS

# ussd
ussd = africastalking.USSD

# functions to use in ussd views

