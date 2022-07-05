from django.contrib import admin

from .models import Cliente, Fornecedor

ADDRESS_FIELDS = (
    'address',
    'address_number',
    'complement',
    'district',
    'city',
    'uf',
    'cep',
)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'razao_social',
        'nome_fantasia',
        'tipo',
        'rg',
        'cpf',
        'cnpj',
        'endereco_entrega',
        'deleted_by',
    ) + ADDRESS_FIELDS
    readonly_fields = ('deleted',)
    list_display_links = ('nome',)
    search_fields = ('nome', 'razao_social', 'nome_fantasia')
    list_filter = ('tipo', 'uf', 'active')


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'razao_social',
        'nome_fantasia',
        'tipo',
        'rg',
        'cpf',
        'cnpj',
        'endereco_entrega',
        'condicao_pagamento',
        'deleted_by',
    ) + ADDRESS_FIELDS
    readonly_fields = ('deleted',)
    list_display_links = ('nome',)
    search_fields = ('nome', 'razao_social', 'nome_fantasia')
    list_filter = ('tipo', 'uf', 'active')
