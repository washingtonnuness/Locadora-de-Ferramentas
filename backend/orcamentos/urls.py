from django.urls import path

from backend.orcamentos import views as v

app_name = 'orcamentos'


urlpatterns = [
    #path('', v.index, name='index'),
    path('create/<int:client_pk>', v.orcamento_create, name='orcamento_create'),
    path('list/', v.orcamento_list, name='orcamento_list'),
    path('search/', v.search, name='search'),
    path('add-row/<int:product_pk>', v.add_row_hx, name='add_row_hx'),
    # path('order-item/<int:pk>/delete/', v.order_item_delete, name='order_item_delete'),
]
