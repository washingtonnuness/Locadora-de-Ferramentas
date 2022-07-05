from django.contrib import admin

from .models import Categoria, Marca, Patrimonio, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    readonly_fields = ('created_by', 'deleted_by', 'deleted',)
    search_fields = ('titulo',)


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'modelo')
    readonly_fields = ('created_by', 'deleted_by', 'deleted',)
    search_fields = ('titulo', 'modelo')


@admin.register(Patrimonio)
class PatrimonioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'produto')
    readonly_fields = ('created_by', 'deleted_by', 'deleted',)
    search_fields = ('titulo', 'produto_titulo')


class PatrimonioInline(admin.TabularInline):
    model = Patrimonio
    extra = 0
    readonly_fields = ('created_by', 'deleted_by', 'deleted',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = (PatrimonioInline,)
    list_display = (
        'codigo',
        'titulo',
        'categoria',
        'marca',
        'preco_compra',
        'preco_diaria',
        'estoque_minimo',
        'estoque_atual',
    )
    list_display_links = ('titulo',)
    readonly_fields = ('created_by', 'deleted_by', 'deleted',)
    search_fields = ('titulo',)
