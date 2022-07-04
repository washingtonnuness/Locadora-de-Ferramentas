from django.urls import path

from backend.fornecedores import views as v

app_name = 'fornecedores'


urlpatterns = [
    path('listar/', v.fornecedores_list, name='fornecedores_list'),
    path('create/', v.fornecedores_create, name='fornecedores_create'),
]
