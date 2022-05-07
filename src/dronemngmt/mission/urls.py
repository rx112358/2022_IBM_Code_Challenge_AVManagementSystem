from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 

from .views import get_dashboard,get_mission_form,get,create_mission,update_mission,delete

urlpatterns=[
path('details',get ),
path('new-mission', get_mission_form,name="new-mission"),
path('create-mission', create_mission,name="create-mission"),
path('update', update_mission),
path('delete', delete)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)