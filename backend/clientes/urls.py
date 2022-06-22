from django.urls import path

from backend.clientes import views as v

app_name = 'clientes'


urlpatterns = [
    #path('', v.index, name='index'),
    path('listar/', v.client_list, name='client_list'),
    path('create/', v.client_create, name='client_create'),
    # path('add-row/', v.add_row_patrimonio_items_hx, name='add_row_patrimonio_items_hx'),
    # path('order-item/<int:pk>/delete/', v.order_item_delete, name='order_item_delete'),
]
