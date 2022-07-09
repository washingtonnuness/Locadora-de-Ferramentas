from django.contrib import admin

from .models import Orcamento, OrcamentoItens


class OrcamentoItensInline(admin.TabularInline):
    model = OrcamentoItens
    extra = 0


@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    inlines = (OrcamentoItensInline,)
    list_display = ('__str__', 'cliente', 'periodo')
    readonly_fields = ('created_by', 'deleted_by', 'deleted',)
    search_fields = ('titulo',)


@admin.register(OrcamentoItens)
class OrcamentoItensAdmin(admin.ModelAdmin):
    list_display = ('orcamento', 'produto', 'patrimonio', 'valor')
