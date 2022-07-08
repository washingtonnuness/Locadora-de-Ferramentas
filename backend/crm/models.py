from django.db import models
from django.urls import reverse

from backend.core.models import (
    Active,
    Address,
    CreatedBy,
    DeletedBy,
    TimeStampedModel
)


class Cliente(TimeStampedModel, Address, CreatedBy, DeletedBy, Active):
    CNPJ = 'CNPJ'
    CPF = 'CPF'

    TIPO_REGISTRO = [
        (CNPJ, CNPJ),
        (CPF, CPF),
    ]

    tipo = models.CharField(max_length=4, choices=TIPO_REGISTRO, default=CNPJ)
    rg = models.CharField('RG', max_length=20, null=True, blank=True)
    cpf = models.CharField('CPF', max_length=11, null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=14, null=True, blank=True)
    nome = models.CharField('Nome Completo', max_length=250)
    razao_social = models.CharField('Razão Social', max_length=250, null=True, blank=True)  # noqa E501
    nome_fantasia = models.CharField('Nome Fantasia', max_length=250, null=True, blank=True)  # noqa E501
    endereco_entrega = models.CharField('Endereço Entrega', max_length=250, null=True, blank=True)  # noqa E501

    def is_upperclass(self):
        return self.tipo in {self.CNPJ, self.CPF}

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    @property
    def codigo(self):
        return str(self.pk).zfill(3)

    def __str__(self):
        return f'{self.nome}'

    def get_absolute_url(self):
        return reverse('crm:cliente_detail', kwargs={'pk': self.pk})


class Fornecedor(TimeStampedModel, Address, CreatedBy, DeletedBy, Active):
    CNPJ = 'CNPJ'
    CPF = 'CPF'

    TIPO_REGISTRO = [
        (CNPJ, CNPJ),
        (CPF, CPF),
    ]

    tipo = models.CharField(max_length=4, choices=TIPO_REGISTRO, default=CNPJ)
    rg = models.CharField('RG', max_length=20, null=True, blank=True)
    cpf = models.CharField('CPF', max_length=11, null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=14, null=True, blank=True)
    nome = models.CharField('Nome Completo', max_length=250)
    razao_social = models.CharField('Razão Social', max_length=250, null=True, blank=True)  # noqa E501
    nome_fantasia = models.CharField('Nome Fantasia', max_length=250, null=True, blank=True)  # noqa E501
    endereco_entrega = models.CharField('Endereço Entrega', max_length=250, null=True, blank=True)  # noqa E501
    condicao_pagamento = models.PositiveIntegerField('Prazo de pagamento', null=True, blank=True)  # noqa E501

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    @property
    def codigo(self):
        return str(self.pk).zfill(3)

    def __str__(self):
        return f'{self.nome}'

    def get_absolute_url(self):
        return reverse('crm:fornecedor_detail', kwargs={'pk': self.pk})
