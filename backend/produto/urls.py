from django.urls import path

from backend.produto import views as v

app_name = 'produto'


urlpatterns = [
    path('', v.produto_list, name='produto_list'),
    path('create/', v.produto_create, name='produto_create'),
    path('add-row/', v.add_row_produto_items_hx, name='add_row_produto_items_hx'),  # noqa E501
]
