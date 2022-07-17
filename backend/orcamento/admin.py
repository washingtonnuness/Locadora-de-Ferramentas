from django.contrib import admin

from .models import Contrato, Orcamento, OrcamentoItens


class OrcamentoItensInline(admin.TabularInline):
    model = OrcamentoItens
    extra = 0


@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    inlines = (OrcamentoItensInline,)
    list_display = ('__str__', 'cliente', 'periodo', 'status', 'active')
    readonly_fields = ('created_by', 'deleted_by', 'deleted',)
    search_fields = ('titulo',)
    list_filter = ('status', 'active',)


@admin.register(OrcamentoItens)
class OrcamentoItensAdmin(admin.ModelAdmin):
    list_display = ('orcamento', 'produto', 'patrimonio', 'quantidade', 'valor')  # noqa E501


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'get_cliente',
        'get_periodo',
        'created',
        'data_final',
        'status',
        'active'
    )
    list_filter = ('status', 'active')

    @admin.display(description='cliente')
    def get_cliente(self, obj):
        return obj.orcamento.cliente

    @admin.display(description='período')
    def get_periodo(self, obj):
        return obj.orcamento.periodo
