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
    Return the recent routes creatd by user
    '''

    try:
        location_id=json.loads(request.body)['loc_id']
        location = Location.objects.get(id=location_id)
        return JsonResponse(location,safe=False)
    
    except :
        print('Location not found')
        return JsonResponse({"Location_error":"Location not found"},status=200)

def create_location(self,request):

    '''
    Create new Location
    '''
    #Getting Location data from form details
    loc_lat            =   request.POST.get('loc_lat')
    loc_lon            =   request.POST.get('loc_lon')

    location=Location(lat=  loc_lat,
    long=loc_lon)

    print(location)

    location.save()

def update_location(self,request):

    '''
    Update Location given Location_id
    '''
    loc_id             =   request.POST.get('loc_id')
    loc_lat            =   request.POST.get('loc_lat')
    loc_lon            =   request.POST.get('loc_lon')

    try:
        #Check if Location exists
        location = Location.objects.get(id=loc_id)

        location.lat=loc_lat
        location.long=loc_lon

        print(location)

        location.save()
    
    except Location.DoesNotExist:
        print('Location not found')
        return JsonResponse({"Location not found":loc_id},status=200)

def delete(self,request):

    '''
    Delete Location given Location_id
    '''

    location_id=json.loads(request.body)['loc_id']

    location = Location.objects.get(id=location_id)
    location.delete()
    return JsonResponse({location_id:" The Location is deleted "},status=200)