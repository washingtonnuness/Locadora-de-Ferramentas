# Generated by Django 4.0.6 on 2022-07-08 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fornecedor',
            options={'ordering': (
                'nome',), 'verbose_name': 'Fornecedor', 'verbose_name_plural': 'Fornecedores'},
        ),
    ]
