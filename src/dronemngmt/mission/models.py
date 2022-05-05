from django.db import models
from device.models import Device
from route.models import Location

from datetime import date,time

# Mission object representing mission details
class Mission(models.Model):

    mission_name            =models.CharField(max_length=2000,default=" ")
    loc                     =models.ManyToManyField(Location)
    device                  =models.ForeignKey(Device ,on_delete=models.CASCADE)
    date                    =models.DateField(default=date.today) 
    time                    =models.TimeField()