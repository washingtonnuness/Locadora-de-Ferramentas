from django.urls import path

from backend.orcamento import views as v

app_name = 'orcamento'


urlpatterns = [
    path('list/', v.OrcamentoListView.as_view(), name='orcamento_list'),
    path('create/', v.orcamento_create, name='orcamento_create'),
    path('search/', v.search, name='search'),
    path('add-row/<int:pk>', v.add_row_hx, name='add_row_hx'),
]
