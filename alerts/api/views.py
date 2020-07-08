from django.shortcuts import render
from django.http import HttpResponse
from . import logic
import json

def index(request):
    comma_seperated_input = request.GET.get("input") or ''
    SERVER_ID, CPU_UTILISATION, MEMORY_UTILIZATION, DISK_UTILIZATION = comma_seperated_input.split(',')
    response=logic.your_alerting_logic(SERVER_ID, CPU_UTILISATION, MEMORY_UTILIZATION, DISK_UTILIZATION)

    response_dict = {"Response":response }
    return HttpResponse(json.dumps(response_dict),content_type = "application/json")


    