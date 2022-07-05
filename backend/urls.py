from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.core.urls')),
    path('crm/', include('backend.crm.urls'), name='crm'),
    path('produto/', include('backend.produto.urls'), name='produto'),
    path('orcamento/', include('backend.orcamento.urls'), name='orcamento'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
