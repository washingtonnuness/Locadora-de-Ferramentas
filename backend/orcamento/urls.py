from django.urls import include, path

from backend.orcamento import views as v

app_name = 'orcamento'


orcamento_patterns = [
    path('', v.OrcamentoListView.as_view(), name='orcamento_list'),  # noqa E501
    path('detail/<int:pk>/', v.OrcamentoDetailView.as_view(), name='orcamento_detail'),  # noqa E501
    path('create/<int:client_pk>/', v.orcamento_create, name='orcamento_create'),  # noqa E501
    path('update/<int:pk>/', v.orcamento_update, name='orcamento_update'),  # noqa E501
    path('produto/preco/', v.produto_preco, name='produto_preco'),  # noqa E501
    path('search/', v.produto_items_search, name='produto_items_search'),  # noqa E501
    path('add-row/', v.add_row_orcamento_items_hx, name='add_row_orcamento_items_hx'),  # noqa E501
    path('invoice/<int:pk>/', v.orcamento_invoice, name='orcamento_invoice'),  # noqa E501
]

contrato_patterns = [
    path('create/<int:orcamento_pk>/', v.contrato_create, name='contrato_create'),  # noqa E501
    path('<int:pk>/', v.ContratoDetailView.as_view(), name='contrato_detail'),  # noqa E501
]

urlpatterns = [
    path('orcamento/', include(orcamento_patterns)),
    path('contrato/', include(contrato_patterns)),
]
