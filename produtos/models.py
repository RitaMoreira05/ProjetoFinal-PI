from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) #unique = True, para que não haja duas categorias com o mesmo nome

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    foto = models.ImageField(upload_to='media/produtos/')
    validade = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome