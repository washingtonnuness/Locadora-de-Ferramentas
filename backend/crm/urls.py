from django.urls import include, path

from backend.crm import views as v

app_name = 'crm'


cliente_urlpatterns = [
    path('', v.cliente_list, name='cliente_list'),
    path('create/', v.cliente_create, name='cliente_create'),
]


fornecedor_urlpatterns = [
    path('', v.fornecedor_list, name='fornecedor_list'),
    path('create/', v.fornecedor_create, name='fornecedor_create'),
]


urlpatterns = [
    path('cliente/', include(cliente_urlpatterns)),
    path('fornecedor/', include(fornecedor_urlpatterns)),
]
