# Generated by Django 5.1.2 on 2025-01-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encomendas', '0004_encomenda_cidade_encomenda_codigo_postal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemencomenda',
            name='total_produto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
