from django.contrib import admin

from .models import Categoria, Marca, Patrimonio, Produtos


@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "delete_at")
    list_display = [f.name for f in Produtos._meta.fields]
    search_fields = ('nome',)


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "delete_at")
    list_display = [f.name for f in Marca._meta.fields]


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "delete_at")
    list_display = [f.name for f in Categoria._meta.fields]


@admin.register(Patrimonio)
class PatrimonioAdmin(admin.ModelAdmin):
    #readonly_fields = ("created_at", "updated_at", "delete_at")
    list_display = [f.name for f in Patrimonio._meta.fields]
