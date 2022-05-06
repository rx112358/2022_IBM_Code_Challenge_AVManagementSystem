from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.views import View

#Models
from mission.models import Mission
from device.models import Device
from route.models import Location


def get(self,request):

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

def create_device(self,request):

    '''
    Create new Device
    '''
    #Getting Device data from form details

    # Device details

    device_name    = request.POST.get(device_name)
    device_model   = request.POST.get(device_model)    

    device=Device(device_name=device_name,device_model=device_model)  

    print(device)

    device.save()

    #Creating the sensors, and adding to device
    sensor_list     =json.loads(request.POST.get('sensors_data'))
    for sensor in sensor_list:
        sensor_name    = sensor[sensor_name]
        sensor_model   = sensor[sensor_model]
        sensor_value   = sensor[sensor_value]
        
        sensor_obj=Sensor.objects.create(sensor_name= sensor_name ,sensor_model= sensor_model,value=sensor_value)
        device.sensors.add(sensor_obj)

def update_device(self,request):

    '''
    Update Device given Device_id
    '''

        # Device details

    device_id      = request.POST.get(device_id)
    device_name    = request.POST.get(device_name)
    device_model   = request.POST.get(device_model)    

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

def delete(self,request):

    '''
    Delete Device given Device_id
    '''

    device_id=json.loads(request.body)['id']

    device = Device.objects.get(id=device_id)
    device.delete()
    return JsonResponse({device_id:" The Device is deleted "},status=200)
