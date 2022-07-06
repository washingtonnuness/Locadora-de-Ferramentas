from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('backend.core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('crm/', include('backend.crm.urls', namespace='crm')),
    path('produto/', include('backend.produto.urls', namespace='produto')),
    path('orcamento/', include('backend.orcamento.urls', namespace='orcamento')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
