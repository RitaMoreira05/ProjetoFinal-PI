# Generated by Django 5.1.2 on 2025-01-18 19:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encomendas', '0003_encomenda_morada'),
    ]

    operations = [
        migrations.AddField(
            model_name='encomenda',
            name='cidade',
            field=models.CharField(default='Cidade não fornecida', max_length=255),
        ),
        migrations.AddField(
            model_name='encomenda',
            name='codigo_postal',
            field=models.CharField(default='0000-000', max_length=8),
        ),
        migrations.AlterField(
            model_name='encomenda',
            name='morada',
            field=models.CharField(default='Morada não fornecida', max_length=255, validators=[django.core.validators.RegexValidator(message='O código postal deve estar no formato XXXX-XXX.', regex='^\\d{4}-\\d{3}$')]),
        ),
    ]
