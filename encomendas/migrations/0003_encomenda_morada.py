# Generated by Django 5.1.2 on 2025-01-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encomendas', '0002_alter_encomenda_options_remove_encomenda_apelido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='encomenda',
            name='morada',
            field=models.CharField(default='Morada não fornecida', max_length=255),
        ),
    ]
