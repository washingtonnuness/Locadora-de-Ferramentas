from django.db import models
from backend.core.models import Active, TimeStampedModel, CreatedBy, DeletedBy


class Produto(TimeStampedModel, CreatedBy, DeletedBy, Active):
    codigo = models.IntegerField('Código')
    nome = models.CharField('Nome', max_length=100)
    categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    marca = models.ForeignKey(
        'Marca',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    preco_compra = models.DecimalField(
        'Preço compra',
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )
    preco_diaria = models.DecimalField(
        'Preço Diária',
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )
    estoque_minimo = models.PositiveIntegerField('Estoque Mínimo', null=True, blank=True)
    estoque_atual = models.PositiveIntegerField('Estoque Atual', null=True, blank=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.nome}'


class Patrimonio(TimeStampedModel, CreatedBy, DeletedBy, Active):
    nome = models.CharField('nome', max_length=100, unique=True)
    produto = models.ForeignKey(
        Produto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='patrimonios',
    )

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Patrimônio'
        verbose_name_plural = 'Patrimônios'

    def __str__(self):
        return f'{self.nome}'


class Marca(TimeStampedModel, CreatedBy, DeletedBy, Active):
    nome = models.CharField(max_length=100, unique=True)
    modelo = models.CharField(max_length=200)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return f'{self.nome}'


class Categoria(TimeStampedModel, CreatedBy, DeletedBy, Active):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return f'{self.nome}'
