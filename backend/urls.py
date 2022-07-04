from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.core.urls')),
    path('produtos/', include('backend.produto.urls'), name='produto'),
    path('clientes/', include('backend.cliente.urls'), name='cliente'),
    path('fornecedores/', include('backend.fornecedores.urls'), name='fornecedores'),
    path('orcamentos/', include('backend.orcamento.urls'), name='orcamento'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
