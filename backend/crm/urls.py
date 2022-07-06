from django.urls import include, path

from backend.crm import views as v

app_name = 'crm'


cliente_urlpatterns = [
    path('', v.ClienteListView.as_view(), name='cliente_list'),  # noqa E501
    path('detail/<int:pk>/', v.ClienteDetailView.as_view(), name='cliente_detail'),  # noqa E501
    path('create/', v.ClienteCreateView.as_view(), name='cliente_create'),  # noqa E501
]


fornecedor_urlpatterns = [
    path('', v.FornecedorListView.as_view(), name='fornecedor_list'),  # noqa E501
    path('detail/<int:pk>/', v.FornecedorDetailView.as_view(), name='fornecedor_detail'),  # noqa E501
    path('create/', v.FornecedorCreateView.as_view(), name='fornecedor_create'),  # noqa E501
]


urlpatterns = [
    path('cliente/', include(cliente_urlpatterns)),
    path('fornecedor/', include(fornecedor_urlpatterns)),
]
