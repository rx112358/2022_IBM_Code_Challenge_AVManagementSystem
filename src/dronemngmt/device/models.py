from django.db import models

# Sensor details
class Sensor(models.Model):

    sensor_name    =models.CharField(max_length=2000,default=" ")
    sensor_model   =models.CharField(max_length=2000,default=" ")    

# Device details
class Device(models.Model):

    device_name    =models.CharField(max_length=2000,default=" ")
    device_model   =models.CharField(max_length=2000,default=" ")    
    sensors        =models.ManyToManyField(Sensor)