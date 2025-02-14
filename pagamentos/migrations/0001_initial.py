# Generated by Django 5.1.2 on 2025-01-15 22:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('numero_cartao', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='O número do cartão deve conter exatamente 16 dígitos.', regex='^\\d{16}$')], verbose_name='Número do Cartão')),
                ('nome_titular', models.CharField(max_length=100, verbose_name='Nome do Titular')),
                ('validade', models.DateField(verbose_name='Data de Validade')),
                ('cvv', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(message='O CVV deve conter exatamente 3 dígitos.', regex='^\\d{3}$')], verbose_name='CVV')),
            ],
        ),
    ]
