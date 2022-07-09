from django.db import models

from backend.core.models import Active, CreatedBy, DeletedBy, TimeStampedModel
from backend.crm.models import Cliente
from backend.produto.models import Patrimonio, Produto


class Orcamento(TimeStampedModel, CreatedBy, DeletedBy, Active):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        related_name='cliente_orcamentos',
        null=True,
        blank=True
    )
    periodo = models.PositiveSmallIntegerField('Período (em dias)', null=True, blank=True)  # noqa E501
    desconto = models.DecimalField(
        'Desconto (%)',
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Em porcentagem'
    )

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'

    def __str__(self):
        return f'{str(self.pk).zfill(3)}'


class OrcamentoItens(models.Model):
    orcamento = models.ForeignKey(
        Orcamento,
        on_delete=models.CASCADE,
        related_name='orcamentos',
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.SET_NULL,
        related_name='produto_orcamentos',
        null=True,
        blank=True
    )
    patrimonio = models.ForeignKey(
        Patrimonio,
        on_delete=models.SET_NULL,
        related_name='patrimonio_orcamentos',
        null=True,
        blank=True
    )
    quantidade = models.PositiveSmallIntegerField('Quantidade', default=1)
    valor = models.DecimalField(
        'Valor',
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Orçamento Item'
        verbose_name_plural = 'Orçamento Itens'

    def __str__(self):
        return f'{self.pk}'
