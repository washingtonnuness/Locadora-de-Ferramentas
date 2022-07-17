from datetime import timedelta

from django.db import models
from django.urls import reverse_lazy

from backend.core.models import Active, CreatedBy, DeletedBy, TimeStampedModel
from backend.crm.models import Cliente
from backend.produto.models import Patrimonio, Produto

STATUS_ORCAMENTO = (
    ('p', 'Pendente'),
    ('f', 'Finalizado'),
    ('c', 'Cancelado'),
)


class Orcamento(TimeStampedModel, CreatedBy, DeletedBy, Active):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        related_name='cliente_orcamentos',
        null=True,
        blank=True
    )
    periodo = models.PositiveSmallIntegerField('Período (em dias)', default=0)
    desconto = models.DecimalField(
        'Desconto (%)',
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Em porcentagem'
    )
    status = models.CharField(max_length=1, choices=STATUS_ORCAMENTO, default='p')  # noqa E501

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'

    def __str__(self):
        return f'{str(self.pk).zfill(3)}'

    def get_absolute_url(self):
        return reverse_lazy('orcamento:orcamento_detail', kwargs={'pk': self.pk})

    def total(self):
        qs = self.orcamentos.filter(orcamento=self.pk).values_list(
            'valor', 'quantidade') or 0
        total = 0 if isinstance(qs, int) else sum(
            map(lambda q: q[0] * q[1], qs))
        return total


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

    def subtotal(self):
        return self.valor * (self.quantidade or 0)


STATUS_CONTRATO = (
    ('p', 'Pendente'),
    ('f', 'Finalizado'),
    ('c', 'Cancelado'),
)


class Contrato(TimeStampedModel, CreatedBy, DeletedBy, Active):
    orcamento = models.OneToOneField(
        Orcamento,
        verbose_name='orçamento',
        related_name='contrato',
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=1, choices=STATUS_CONTRATO, default='p')  # noqa E501

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'contrato'
        verbose_name_plural = 'contratos'

    @property
    def codigo(self):
        return str(self.pk).zfill(3)

    def __str__(self):
        return f'{self.codigo}'

    @property
    def data_final(self):
        return self.created + timedelta(self.orcamento.periodo)

    def get_absolute_url(self):
        return reverse_lazy('orcamento:contrato_detail', pk=self.pk)
