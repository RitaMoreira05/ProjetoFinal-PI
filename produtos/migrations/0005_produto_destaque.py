# Generated by Django 5.1.2 on 2024-11-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_alter_produto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='destaque',
            field=models.BooleanField(default=False),
        ),
    ]
