from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produto
from django.conf import settings
from django.core.validators import RegexValidator

class Encomenda(models.Model):
    ESTADO_CHOICES = [
        ('pendente', 'Pendente'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    morada = models.CharField(max_length=255, default='Morada não fornecida',
                              validators=[
                                    RegexValidator(
                                        regex=r'^\d{4}-\d{3}$',
                                        message="O código postal deve estar no formato XXXX-XXX."
                                    )
                              ])
    codigo_postal = models.CharField(max_length=8, default='0000-000')
    cidade = models.CharField(max_length=255, default='Cidade não fornecida')
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendente')
    produtos = models.ManyToManyField(Produto, through='ItemEncomenda')

    def __str__(self):
        return f"Encomenda #{self.id} - {self.user.username}"
    
    # No seu modelo de Encomenda
    def get_estado_color(self):
        if self.estado == 'pendente':
            return 'red'  # Para encomendas pendentes
        elif self.estado == 'enviado':
            return 'blue'  # Para encomendas enviadas
        elif self.estado == 'entregue':
            return 'green'  # Para encomendas entregues
        elif self.estado == 'cancelado':
            return 'gray'  # Para encomendas canceladas
        else:
            return 'black'  # Para casos em que o estado não é identificado



class ItemEncomenda(models.Model):
    encomenda = models.ForeignKey(Encomenda, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    total_produto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome} (Encomenda #{self.encomenda.id})'
