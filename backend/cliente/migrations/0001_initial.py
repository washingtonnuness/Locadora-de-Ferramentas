# Generated by Django 4.0.4 on 2022-06-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[
                 ('CNPJ', 'CNPJ'), ('CPF', 'CPF')], default='CNPJ', max_length=4)),
                ('cnpj', models.IntegerField(
                    blank=True, null=True, verbose_name='CNPJ')),
                ('rg', models.IntegerField(verbose_name='RG')),
                ('cpf', models.IntegerField(verbose_name='CPF')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome Completo')),
                ('razaoSocial', models.CharField(
                    max_length=250, verbose_name='Razão Social')),
                ('nomeFantasia', models.CharField(
                    max_length=250, verbose_name='Nome Fantasia')),
                ('endereco', models.CharField(
                    max_length=250, verbose_name='Endereço:')),
                ('endereco2', models.CharField(
                    max_length=250, verbose_name='Endereço Entrega:')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado')),
                ('cep', models.CharField(max_length=100, verbose_name='Cep')),
                ('delete_user', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('checkbox', models.BooleanField(
                    max_length=100, verbose_name='Desativar')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('delete_at', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ('tipo', 'nome', 'nomeFantasia'),
            },
        ),
    ]
