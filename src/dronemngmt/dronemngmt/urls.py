from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static 
from django.urls import path, include,re_path

from mission.views import get_dashboard

urlpatterns = [
    path('home',get_dashboard ),
    path('admin/', admin.site.urls),
    path('mission/',include('mission.urls')),
    path('device/',include('device.urls')),
    path('location/',include('route.urls'))
]
