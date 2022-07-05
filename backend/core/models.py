from django.contrib.auth.models import User
from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class TimeStampedModel(models.Model):
    created = models.DateTimeField('criado em', auto_now_add=True)
    modified = models.DateTimeField('modificado em', auto_now=True)
    deleted = models.DateTimeField('deletado em', null=True, blank=True)

    class Meta:
        abstract = True


class CreatedBy(models.Model):
    created_by = models.ForeignKey(
        User,
        verbose_name='criado por',
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_created_by',
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class DeletedBy(models.Model):
    deleted_by = models.ForeignKey(
        User,
        verbose_name='deletado por',
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_deleted_by',
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class Address(models.Model):
    address = models.CharField(
        'endereço',
        max_length=100,
        null=True,
        blank=True
    )
    address_number = models.IntegerField('número', null=True, blank=True)
    complement = models.CharField(
        'complemento',
        max_length=100,
        null=True,
        blank=True
    )
    district = models.CharField(
        'bairro',
        max_length=100,
        null=True,
        blank=True
    )
    city = models.CharField('cidade', max_length=100, null=True, blank=True)
    uf = models.CharField(
        'UF',
        max_length=2,
        choices=STATE_CHOICES,
        null=True,
        blank=True
    )
    cep = models.CharField('CEP', max_length=9, null=True, blank=True)
    country = models.CharField(
        'país',
        max_length=50,
        default='Brasil',
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class Active(models.Model):
    active = models.BooleanField('ativo', default=True)
    exist_deleted = models.BooleanField(
        'existe/deletado',
        default=True,
        help_text='Se for True o item existe. Se for False o item foi deletado.'
    )

    class Meta:
        abstract = True
