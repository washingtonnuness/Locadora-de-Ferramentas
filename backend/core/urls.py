from xml.etree.ElementInclude import include
from django.urls import path, include
from django.conf import settings
from django.contrib import admin

from backend.core import views as v

app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls'))
]
