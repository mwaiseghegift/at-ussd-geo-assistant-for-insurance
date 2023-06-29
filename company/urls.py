from .views import ussd_view
from django.urls import path

app_name = 'company'

urlpatterns = [
    path('ussd/', ussd_view, name='ussd'),
]