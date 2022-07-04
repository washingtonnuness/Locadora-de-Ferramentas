from django.urls import path

from backend.cliente import views as v

app_name = 'cliente'


urlpatterns = [
    path('listar/', v.cliente_list, name='cliente_list'),
    path('create/', v.cliente_create, name='cliente_create'),
]
