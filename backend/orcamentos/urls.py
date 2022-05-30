from django.urls import path

from backend.orcamentos import views as v

app_name = 'orcamentos'


urlpatterns = [
    path('<int:client_pk>/', v.add_orcamento, name='add_orcamento'),
    path('listar/', v.listOrcamentos, name='listOrcamentos'),
    path('search/', v.search, name='search'),
    path('add-row/<int:product_pk>', v.add_produtc_row, name='add_row_hx'),
    path('clear/', v.clear, name='clear'),

    # path('order-item/<int:pk>/delete/', v.order_item_delete, name='order_item_delete'),
]