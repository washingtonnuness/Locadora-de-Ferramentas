from django.db import models

from backend.core.models import Active, Address, TimeStampedModel


class Cliente(TimeStampedModel, Address, Active):
    CNPJ = 'CNPJ'
    CPF = 'CPF'

    TIPO_REGISTRO = [
        (CNPJ, CNPJ),
        (CPF, CPF),
    ]

    tipo = models.CharField(max_length=4, choices=TIPO_REGISTRO, default=CNPJ)
    cnpj = models.IntegerField("CNPJ", null=True, blank=True)
    rg = models.IntegerField("RG", null=True, blank=True)
    cpf = models.IntegerField("CPF", null=True, blank=True)
    nome = models.CharField("Nome Completo", max_length=250)
    razao_social = models.CharField("Razão Social", max_length=250)
    nome_fantasia = models.CharField("Nome Fantasia", max_length=250)
    endereco2 = models.CharField("Endereço Entrega:", max_length=250)
    delete_user = models.CharField(max_length=100, null=True, blank=True)

    def is_upperclass(self):
        return self.tipo in {self.CNPJ, self.CPF}

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.nome}'
