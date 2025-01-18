from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produto
from django.conf import settings

class Encomenda(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    morada = models.CharField(max_length=255, default='Morada não fornecida')


class ItemEncomenda(models.Model):
    encomenda = models.ForeignKey(Encomenda, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome} (Encomenda #{self.encomenda.id})'
