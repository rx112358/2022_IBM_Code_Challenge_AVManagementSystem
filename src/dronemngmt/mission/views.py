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

import json

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

def get_recent_missions(request):

    '''
    Return the recent missions creatd by user
    '''
    try:
        missions=Mission.objects.all().reverse()[:10]
        mission_obj=[]

        for mission in missions:
            #print(mission.locations.values())
            start_loc=[mission.locations.values()[0]['lat'],mission.locations.values()[0]['long']]
            end_loc=[mission.locations.values()[1]['lat'],mission.locations.values()[1]['long']]
            name=mission.mission_name
            mission_obj.append({'name':name,'start':start_loc,'end':end_loc})
        
        context = {'missions': mission_obj }
        response=render(request, "default.html",context)
        return response
    
    except Mission.DoesNotExist():
        print('Not enough missions created')
        return JsonResponse({"mission_error":"Not enough missions"},status=200)

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
    data = json.loads(request.body)
    print(data)
    
    mission_name = data['mission_name']
    #device_id    = data['device_id']
    date         = data['date']
    time         = data['time']

    mission=Mission(mission_name=mission_name,date=date,time=time)

    mission.save()
    print(mission)

        #Creating the locations, and adding to device
    location_list      =json.loads(data['locations'])
    print(location_list)
    for location in location_list:
        location_lat   = location['lat']
        location_lon   = location['long']
        
        location_obj=Location.objects.create(lat=location_lat,long=location_lon)
        print(location_obj)
        mission.locations=location_obj
    
    return JsonResponse({"Mission created":mission.id},status=200)

def update_mission(request):

    '''
    Update mission given mission_id
    '''
    data = json.loads(request.body)
    
    mission_name            =   data['mission_name']
    mission_id              =   data['mission_id']
    device                  =   data['device_id']
    date                    =   data['date']
    time                    =   data['time']

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
        return jsonResponse({"Mission not found":mission_id},status=200)

def delete(request):

    '''
    Delete mission given mission_id
    '''

    mission_id=json.loads(request.body)['id']

    mission = Mission.objects.get(mission_id=mission_id)
    mission.delete()
    return JsonResponse({mission_id:" The mission is deleted "},status=200)