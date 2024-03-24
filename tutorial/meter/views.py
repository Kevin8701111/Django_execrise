from rest_framework.views import APIView
# from rest_framework import viewsets
# from meter.models import MeterValue
# from tutorial.meter.serializers import ProductSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from meter.meter_action import oneplusone


class Meter_AppReq(APIView):
    @csrf_exempt
    def get(self, request, **kwargs):
        meter_address =  kwargs.get('address')
        meter_ip = '192.168.0.123'
        meter_model = '123'
        meter_phase = '3'
        meter_A1 = oneplusone.Meter(ip = meter_ip, model= meter_model, phase=meter_phase)
        address_value = meter_A1.meter_address_value(address=meter_address)
        return HttpResponse(address_value)