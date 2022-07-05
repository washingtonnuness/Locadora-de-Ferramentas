from xml.etree.ElementInclude import include

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from backend.core import views as v

app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls'))
]
