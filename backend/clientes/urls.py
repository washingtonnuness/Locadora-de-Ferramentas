from django.urls import path

from SOE.clientes import views as v

app_name = 'clientes'


urlpatterns = [
    #path('', v.index, name='index'),
    path('listar/', v.listarClientes, name='listarClientes'),
    path('create/', v.inserir, name='cadClientes'),
    # path('add-row/', v.add_row_patrimonio_items_hx, name='add_row_patrimonio_items_hx'),
    # path('order-item/<int:pk>/delete/', v.order_item_delete, name='order_item_delete'),
]