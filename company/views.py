from django.shortcuts import render
from .models import InsuranceCompany, InsuranceHospital, InsuranceCustomer, InsuranceClaim
from decouple import config
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# import package
import africastalking

# Initialize SDK
username = "dekut-hack-g"    # use 'sandbox' for development in the test environment
api_key = config('AFRICASTALKING_API_KEY')      # use your sandbox app API key for development in the test environment

africastalking.initialize(username, api_key)

# Initialize a service i.e SMS, USSD
sms = africastalking.SMS

# ussd
ussd = africastalking.USSD

# functions to use in ussd views

def get_nearest_hospital(location, insurance_company):
    nearest_hospitals = InsuranceHospital.objects.annotate(
        distance=Distance('location', location)).filter(
        distance__lte=10000, insurance_company=insurance_company).order_by('distance')
    return nearest_hospitals

def get_insurance_companies():
    insurance_companies = InsuranceCompany.objects.all()
    return insurance_companies


# ussd view
@csrf_exempt
def ussd_view(request):

    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON Welcome to Alchemists Insurance. \n"
            response += "1. Check Insurances Available Near You \n"
            response += "2. Check Nearest Hospital For Your Insurance \n"
            response += "3. Make Enquiry on Insurance \n"

        elif text == "1":
            response = "CON Choose Insurance Company \n"
            insurance_companies = get_insurance_companies()
            for insurance_company in insurance_companies:
                response += str(insurance_company.id) + ". " + insurance_company.name + "\n"

        elif text == f"1*{text}":
            response = "Enter Your Location \n"
            insurance_company = InsuranceCompany.objects.get(id=text)
            session = ussd.create_session(phone_number, service_code, session_id)
            session['insurance_company'] = insurance_company.id
            session.save()



        elif text == "2":
            insurance_companies = get_insurance_companies()
            response = "CON Choose Insurance Company \n"
            for insurance_company in insurance_companies:
                response += str(insurance_company.id) + ". " + insurance_company.name + "\n"

        else:
            response = "CON Invalid option. Please try again." 

        return HttpResponse(response)