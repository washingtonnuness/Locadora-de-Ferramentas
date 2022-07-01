from django.contrib import admin

from .models import Categoria, Marca, Patrimonio, Produto


class PatrimonioInline(admin.TabularInline):
    model = Patrimonio
    extra = 0


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = (PatrimonioInline,)
    readonly_fields = ("created_at", "updated_at", "delete_at")
    list_display = [f.name for f in Produto._meta.fields if f.name != 'id']
    search_fields = ('nome',)


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "delete_at")
    list_display = [f.name for f in Marca._meta.fields if f.name != 'id']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "delete_at")
    list_display = [f.name for f in Categoria._meta.fields if f.name != 'id']


@admin.register(Patrimonio)
class PatrimonioAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Patrimonio._meta.fields if f.name != 'id']
