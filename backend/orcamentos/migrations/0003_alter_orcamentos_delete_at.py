# Generated by Django 4.0.4 on 2022-05-30 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentos', '0002_remove_orcamentos_patrimonio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamentos',
            name='delete_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]