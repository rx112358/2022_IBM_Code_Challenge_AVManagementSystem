from django.db import models

# Location object representing a location point of a mission
class Location(models.Model):

    long        =models.FloatField(default=0.0)
    lat         =models.FloatField(default=0.0)
    locname     =models.CharField(max_length=2000,default=" ")