from django.db import models

# Create your models here.


class Produtos(models.Model):
    codigo = models.IntegerField("Código")
    id_grupo = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    id_marca = models.ForeignKey(
        'Marca',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    nome = models.CharField("Nome", max_length=100)
    valor_Compra = models.CharField("Preço compra", max_length=100)
    valor_Locacao = models.CharField("Preço Diária", max_length=100)
    estoque_minimo = models.CharField("Estoque minimo", max_length=100, null=True, blank=True)
    qnt_estoque = models.CharField("Qnt em Estoque", max_length=100, null=True, blank=True)
    estoque_total = models.CharField("Estoque total", max_length=100, null=True, blank=True)
    created_user = models.CharField(max_length=100, null=True, blank=True)
    delete_user = models.CharField(max_length=100, null=True, blank=True) 
    checkbox = models.BooleanField("Excluir", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=False, null=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ('id_grupo', 'id_marca', 'nome')
        
class Patrimonio(models.Model):
    produtoPatrimonio = models.ForeignKey(
        Produtos,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='patrimonios',
    )
    patrimonio = models.CharField(max_length=100, unique=True)
    created_user = models.CharField(max_length=100, null=True, blank=True)
    delete_user = models.CharField(max_length=100, null=True, blank=True) 
    checkbox = models.BooleanField("Excluir", max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    delete_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    
    class Meta:
        ordering = ('patrimonio',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.produtoPatrimonio.nome, self.patrimonio)

class Marca(models.Model):
    marca = models.CharField(max_length=100, unique=True)
    modelo = models.CharField(max_length=200, unique=False)
    created_user = models.CharField(max_length=100, null=True, blank=True)
    delete_user = models.CharField(max_length=100, null=True, blank=True) 
    checkbox = models.BooleanField("Excluir", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=False, null=True)

    class Meta:
        ordering = ('marca','modelo')

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.marca, self.modelo)

class Categoria(models.Model):
    categoria = models.CharField(max_length=100, unique=True)
    created_user = models.CharField(max_length=100, null=True, blank=True)
    delete_user = models.CharField(max_length=100, null=True, blank=True) 
    checkbox = models.BooleanField("Excluir", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=False, null=True)

    class Meta:
        ordering = ('categoria',)

    def __str__(self):
        return self.categoria

