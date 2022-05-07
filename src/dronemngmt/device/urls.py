from django.urls import path
from django.conf import settings

from .views import get,create_device,update_device,delete

urlpatterns=[
path('details',get ),
path('new-device', create_device),
path('update', update_device),
path('delete', delete)
]
