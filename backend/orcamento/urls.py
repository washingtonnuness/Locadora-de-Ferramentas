from django.urls import path

from backend.orcamento import views as v

app_name = 'orcamento'


urlpatterns = [
    path('', v.OrcamentoListView.as_view(), name='orcamento_list'),  # noqa E501
    path('create/<int:client_pk>/', v.orcamento_create, name='orcamento_create'),  # noqa E501
    path('update/<int:pk>/', v.orcamento_update, name='orcamento_update'),  # noqa E501
    path('produto/preco/', v.produto_preco, name='produto_preco'),
    path('search/', v.produto_items_search, name='produto_items_search'),  # noqa E501
    path('add-row/', v.add_row_orcamento_items_hx, name='add_row_orcamento_items_hx'),  # noqa E501
    path('invoice/', v.invoice, name='orcamento_invoice'),  # noqa E501
]
