# Generated by Django 4.0.4 on 2022-07-05 10:23

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
                ('created', models.DateTimeField(
                    auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(
                    auto_now=True, verbose_name='modificado em')),
                ('deleted', models.DateTimeField(
                    blank=True, null=True, verbose_name='deletado em')),
                ('address', models.CharField(blank=True,
                 max_length=100, null=True, verbose_name='endereço')),
                ('address_number', models.IntegerField(
                    blank=True, null=True, verbose_name='número')),
                ('complement', models.CharField(blank=True,
                 max_length=100, null=True, verbose_name='complemento')),
                ('district', models.CharField(blank=True,
                 max_length=100, null=True, verbose_name='bairro')),
                ('city', models.CharField(blank=True,
                 max_length=100, null=True, verbose_name='cidade')),
                ('uf', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), (
                    'PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, null=True, verbose_name='UF')),
                ('cep', models.CharField(blank=True,
                 max_length=9, null=True, verbose_name='CEP')),
                ('country', models.CharField(blank=True, default='Brasil',
                 max_length=50, null=True, verbose_name='país')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('exist_deleted', models.BooleanField(
                    default=True, help_text='Se for True o item existe. Se for False o item foi deletado.', verbose_name='existe/deletado')),
                ('tipo', models.CharField(choices=[
                 ('CNPJ', 'CNPJ'), ('CPF', 'CPF')], default='CNPJ', max_length=4)),
                ('cnpj', models.IntegerField(
                    blank=True, null=True, verbose_name='CNPJ')),
                ('rg', models.IntegerField(blank=True, null=True, verbose_name='RG')),
                ('cpf', models.IntegerField(blank=True, null=True, verbose_name='CPF')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome Completo')),
                ('razao_social', models.CharField(
                    max_length=250, verbose_name='Razão Social')),
                ('nome_fantasia', models.CharField(
                    max_length=250, verbose_name='Nome Fantasia')),
                ('endereco2', models.CharField(
                    max_length=250, verbose_name='Endereço Entrega:')),
                ('delete_user', models.CharField(
                    blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ('nome',),
            },
        ),
    ]
