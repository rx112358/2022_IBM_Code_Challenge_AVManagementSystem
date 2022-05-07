from django.db import models
from device.models import Device
from route.models import Location

from datetime import date,time

# Mission object representing mission details
class Mission(models.Model):

    mission_name            =models.CharField(max_length=2000,default="mission_default")
    mission_id              =models.CharField(max_length=2000,default="M")
    locations               =models.ManyToManyField(Location,null=True,related_name="start")
    device                  =models.ForeignKey(Device ,on_delete=models.CASCADE,null=True,default=1000)
    date                    =models.DateField(default=date.today)  # YYYY-MM-DD
    time                    =models.TimeField()

    '''
    def save(self,*args,**kwargs):
        def generate_mission_id(self):
            prefix="M"
            return str(prefix+str(self.id+default_mission_count) )
        self.misssion_id=generate_mission_id(self)
        super(Mission,self).save(*args,**kwargs)
    '''