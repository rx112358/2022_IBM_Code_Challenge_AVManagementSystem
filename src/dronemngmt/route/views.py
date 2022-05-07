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

def get_route(request):

    '''
    Return the recent missions creatd by user
    '''

    response=render(request, "route.html")
    return response


def get(request):

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

def create_location(request):

    '''
    Create new Location
    '''
    #Getting Location data from form details
    data = json.loads(request.body)
    loc_lat            =   data['loc_lat']
    loc_lon            =   data['loc_lon']

    location=Location(lat=  loc_lat,
    long=loc_lon)

    print(location)

    location.save()

def update_location(request):

    '''
    Update Location given Location_id
    '''
    data = json.loads(request.body)
    loc_id             =   data['loc_id']
    loc_lat            =   data['loc_lat']
    loc_lon            =   data['loc_lon']

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

def delete(request):

    '''
    Delete Location given Location_id
    '''

    location_id=json.loads(request.body)['loc_id']

    location = Location.objects.get(id=location_id)
    location.delete()
    return JsonResponse({location_id:" The Location is deleted "},status=200)
