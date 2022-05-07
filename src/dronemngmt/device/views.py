from django.views import View
from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt,csrf_protect

from django.contrib import messages

from django.db.models import Count

from django.shortcuts import redirect

import json
from django.core import serializers

#Models
from mission.models import Mission
from device.models import Device
from route.models import Location


def get(request):

    '''
    Return a device given the device id
    '''

    try:
        device_id=json.loads(request.body)['id']
        device = Device.objects.get(id=device_id)
        return JsonResponse(device,safe=False)
    
    except :
        print('Device not found')
        return JsonResponse({"device_error":"Device not found"},status=200)

def create_device(request):

    '''
    Create new Device
    '''
    #Getting Device data from form details

    # Device details
    data = json.loads(request.body)
    device_name    = data[device_name]
    device_model   = data[device_model]  

    device=Device(device_name=device_name,device_model=device_model)  

    print(device)

    device.save()

    #Creating the sensors, and adding to device
    sensor_list     =json.loads(data('sensors_data'))
    for sensor in sensor_list:
        sensor_name    = sensor[sensor_name]
        sensor_model   = sensor[sensor_model]
        sensor_value   = sensor[sensor_value]
        
        sensor_obj=Sensor.objects.create(sensor_name= sensor_name ,sensor_model= sensor_model,value=sensor_value)
        device.sensors.add(sensor_obj)

def update_device(request):

    '''
    Update Device given Device_id
    '''

        # Device details
    data = json.loads(request.body)
    device_id      = data[device_id]
    device_name    = data[device_name]
    device_model   = data[device_model]    

    try:
        #Check if Device exists
        device = Device.objects.get(id=device_id)

        device.device_name = device_name 
        device.device_model= device_model

        print(device)

        device.save()
    
    except Device.DoesNotExist:
        print('Device not found')
        return JsonResponse({"Device not found":device_id},status=200)

def delete(request):

    '''
    Delete Device given Device_id
    '''

    device_id=json.loads(request.body)['id']

    device = Device.objects.get(id=device_id)
    device.delete()
    return JsonResponse({device_id:" The Device is deleted "},status=200)
