from django.urls import path

from backend.clientes import views as v

app_name = 'clientes'


urlpatterns = [
    path('listar/', v.client_list, name='client_list'),
    path('create/', v.client_create, name='client_create'),
]
