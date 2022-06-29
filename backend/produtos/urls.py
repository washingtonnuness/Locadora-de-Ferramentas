from django.urls import path

from backend.produtos import views as v

app_name = 'produto'


urlpatterns = [
    path('', v.product_list, name='product_list'),
    path('create/', v.product_create, name='product_create'),
    path('add-row/', v.add_row_product_items_hx, name='add_row_product_items_hx'),  # noqa E501
]
