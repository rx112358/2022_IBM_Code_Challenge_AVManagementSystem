from django.urls import path
from django.conf import settings

from .views import get_route,get,create_location,update_location,delete

urlpatterns=[
path('monitor-mission',get_route ,name="monitor-mission"),
path('details',get ),
path('new-location', create_location),
path('update', update_location),
path('delete', delete)
]
