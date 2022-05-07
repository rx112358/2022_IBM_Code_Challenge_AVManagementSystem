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

def get_dashboard(request):

    '''
    Return the recent missions creatd by user
    '''

    response=render(request, "index.html")
    return response

def get_mission_form(request):

    '''
    Return the recent missions creatd by user
    '''

    response=render(request, "mission.html")
    return response

def get(request):

    '''
    Return the recent missions creatd by user
    '''

    try:
        mission=Mission.objects.values().reverse()[:10]
        return JsonResponse(mission,safe=False)
    
    except :
        print('Not enough missions created')
        return JsonResponse({"mission_error":"Not enough missions"},status=200)

def create_mission(request):

    '''
    Create new mission
    '''
    #Getting mission data from form details
    mission_name            =   request.POST.get('mission_name')
    #device_id               =   request.POST.get('device_id'   )
    date                    =   request.POST.get('date'        )
    time                    =   request.POST.get('time'        )

    mission=Mission(mission_name=mission_name      
    ,date=date         
    ,time=time)

    print(mission)

    mission.save()

        #Creating the locations, and adding to device
    location_list      =request.POST.get('locations_data')
    for location in location_list:
        location_lat   = location['lat']
        location_lon   = location['long']
        
        location_obj=location.objects.create(lat=location_lat,long=location_lon)
        mission.locations.add(location_obj)

def update_mission(request):

    '''
    Update mission given mission_id
    '''

    mission_name            =   request.POST.get('mission_name' )
    mission_id              =   request.POST.get('mission_id' )
    device                  =   request.POST.get('device_id' )
    date                    =   request.POST.get('date' )
    time                    =   request.POST.get('time' )

    try:
        #Check if mission exists
        mission = Mission.objects.get(mission_id=mission_id)

        mission.mission_name=mission_name       
        mission.device      =device       
        mission.date        =date         
        mission.time        =time

        print(mission)

        mission.save()
    
    except Mission.DoesNotExist:
        print('Mission not found')
        return JsonResponse({"Mission not found":mission_id},status=200)

def delete(request):

    '''
    Delete mission given mission_id
    '''

    mission_id=json.loads(request.body)['id']

    mission = Mission.objects.get(mission_id=mission_id)
    mission.delete()
    return JsonResponse({mission_id:" The mission is deleted "},status=200)
