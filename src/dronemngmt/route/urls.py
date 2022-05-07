from django.urls import path
from django.conf import settings

from .views import get,create_location,update_location,delete

urlpatterns=[
path('details',get ),
path('new-location', create_location),
path('update', update_location),
path('delete', delete)
]
