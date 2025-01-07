from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.utils.text import slugify

class Categoria(models.Model):
    """
    Representa uma categoria de produtos.

    Atributos:
        nome (str): O nome da categoria.
        slug (str): Um identificador único para a categoria, gerado automaticamente a partir do nome se não for fornecido.
    """
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True) #unique = True, para que não haja duas categorias com o mesmo nome

    def __str__(self):
        """
        Retorna uma representação em string da categoria, que é o seu nome.
        """
        return self.nome
    
    def save(self, *args, **kwargs):
        """
        Subscreve o método save para gerar automaticamente o slug a partir do nome, se não for fornecido.
        """
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

class Produto(models.Model):
    """
    Representa um produto.

    Atributos:
        nome (str): O nome do produto.
        slug (str): Um identificador único para o produto, gerado automaticamente a partir do nome.
        descricao (str): A descrição do produto.
        preco (decimal): O preço do produto, que deve ser um valor positivo.
        stock (int): A quantidade em stock do produto.
        foto (ImageField): Uma imagem do produto.
        validade (date): A data de validade do produto.
        categoria (ForeignKey): A categoria à qual o produto pertence.
        destaque (bool): Indica se o produto é um destaque.
    """
    nome = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True) #blank = True, para que o campo não seja obrigatório
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    stock = models.PositiveIntegerField()
    foto = models.ImageField(upload_to='media/produtos/')
    validade = models.DateField()
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        """
        Retorna uma representação em string do produto, que é o seu nome.
        """
        return self.nome
    
    def clean(self):
        """
        Valida os campos do produto.
        
        Levanta uma ValidationError se o preço for negativo ou se a validade for uma data passada.
        """
        # Verifica se o preço é negativo
        if self.preco < 0:
            raise ValidationError("O preço não pode ser negativo.")
        
        # Verifica se a validade é uma data passada
        if self.validade < timezone.now().date():
            raise ValidationError("A validade deve ser uma data futura.")
        
    def save(self, *args, **kwargs):
        """
        Subscreve o método save para gerar automaticamente o slug a partir do nome, se não for fornecido.
        """
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)