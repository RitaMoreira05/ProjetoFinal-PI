from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.

class Utilizador(AbstractUser):
    """
    Representa um utilizador do sistema.

    Atributos:
        nome (str): O nome do utilizador.
        apelido (str): O apelido do utilizador.
        email (EmailField): O endereço de e-mail do utilizador, que deve ser único.
        telefone (str): O número de telefone do utilizador, que pode ser opcional.
        morada (str): A morada do utilizador.
        codigo_postal (str): O código postal do utilizador, validado com um RegexValidator.
        nif (str): O número de identificação fiscal do utilizador.
    """
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=9, blank=True, null=True)
    morada = models.CharField(max_length=100)
    codigo_postal = models.CharField(
        max_length=8, 
        validators=[RegexValidator(r'^\d{4}-\d{3}$', message='Código postal inválido')]
    )
    nif = models.CharField(max_length=9)