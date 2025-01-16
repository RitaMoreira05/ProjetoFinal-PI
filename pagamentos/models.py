from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, ValidationError
from django.utils import timezone

class Compra(models.Model):
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.01)],  # Garante valores maiores que 0
    )
    numero_cartao = models.CharField(
        max_length=16,
        validators=[
            RegexValidator(
                regex=r'^\d{16}$',
                message="O número do cartão deve conter exatamente 16 dígitos."
            )
        ],
        verbose_name="Número do Cartão"
    )
    nome_titular = models.CharField(max_length=100, verbose_name="Nome do Titular")
    validade = models.DateField(verbose_name="Data de Validade")
    cvv = models.CharField(
        max_length=3,
        validators=[
            RegexValidator(
                regex=r'^\d{3}$',
                message="O CVV deve conter exatamente 3 dígitos."
            )
        ],
        verbose_name="CVV"
    )

    def _str_(self):
        return f"Compra de {self.valor} por {self.nome_titular}"
    
    def clean(self):
        """
        Valida os campos do produto.
        
        Levanta uma ValidationError se o preço for negativo ou se a validade for uma data passada.
        """
        # Verifica se o preço é negativo
        if self.valor < 0:
            raise ValidationError("O preço não pode ser negativo.")
        
        # Verifica se a validade é uma data passada
        if self.validade < timezone.now().date():
            raise ValidationError("A validade deve ser uma data futura.")
