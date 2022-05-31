from django.urls import path
from backend.produtos import views as v
app_name = 'produto'


urlpatterns = [
    path('', v.product_list, name='product_list'),
    path('create/', v.product_create, name='product_create'),
    path('add-row/', v.add_row_product_items_hx, name='add_row_product_items_hx'),
    #path('product/price/', v.product_price, name='product_price'),
    #path('<int:pk>/update/', v.order_update, name='order_update'),
    #path('order-item/<int:pk>/delete/', v.order_item_delete, name='order_item_delete'),
]
