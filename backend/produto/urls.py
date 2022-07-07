from django.urls import path

from backend.produto import views as v

app_name = 'produto'


urlpatterns = [
    path('', v.ProdutoListView.as_view(), name='produto_list'),  # noqa E501
    path('detail/<int:pk>/', v.ProdutoDetailView.as_view(), name='produto_detail'),  # noqa E501
    path('create/', v.produto_create, name='produto_create'),  # noqa E501
    path('add-row/', v.add_row_produto_items_hx, name='add_row_produto_items_hx'),  # noqa E501
    path('produto-search/', v.produto_items_search, name='produto_items_search'),  # noqa E501
]
