from django.urls import path

from SOE.produtos import views as v

app_name = 'produtos'


urlpatterns = [
    path('', v.index, name='index'),
    path('listar/', v.listProdutos, name='listarProdutos'),
    path('create/', v.inserir, name='createProdutos'),
    # path('add-row/', v.add_row_patrimonio_items_hx, name='add_row_patrimonio_items_hx'),
    path('order-item/<int:pk>/delete/', v.order_item_delete, name='order_item_delete'),
]
