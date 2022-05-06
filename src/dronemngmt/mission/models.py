from django.db import models
from device.models import Device
from route.models import Location

from datetime import date,time

# Mission object representing mission details
class Mission(models.Model):

    default_mission_count=1000

    mission_name            =models.CharField(max_length=2000,default="mission_default")
    mission_id              =models.CharField(max_length=2000,default="M")
    locations               =models.ManyToManyField(Location,null=True)
    device                  =models.ForeignKey(Device ,on_delete=models.CASCADE,null=True)
    date                    =models.DateField(default=date.today) 
    time                    =models.TimeField()

    def generate_mission_id(self):
        prefix="M"
        return str(prefix+str(self.id+default_mission_count) )
    
    def save(self,*args,**kwargs):
        self.misssion_id=generate_mission_id(self)
        super(Mission,self).save(*args,**kwargs)