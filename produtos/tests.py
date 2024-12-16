from django.test import TestCase
from django.urls import reverse
from .models import Produto, Categoria
from django.core.files.uploadedfile import SimpleUploadedFile

class ProdutoCriacaoTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Categoria Teste')
        self.produto_data = {
            'nome': 'Produto Teste',
            'descricao': 'Descrição do produto',
            'preco': 10.50,
            'stock': 100,
            'foto': SimpleUploadedFile("image.jpg", b"file_content"),
            'validade': '2025-12-31',
            'categoria': self.categoria,
            'destaque': True
        }

    def test_criar_produto(self):
        categoria = Categoria.objects.create(nome="Categoria Teste")
        produto = Produto.objects.create(nome="Produto Teste", categoria=categoria)
        produto_salvo = Produto.objects.get(nome="Produto Teste")
        self.assertEqual(produto_salvo.nome, "Produto Teste")
    
    def test_criar_produto_com_imagem(self):
        categoria = Categoria.objects.create(nome="Categoria Teste")
        imagem = SimpleUploadedFile("imagem.jpg", b"file_content", content_type="image/jpeg")
        produto = Produto.objects.create(nome="Produto Teste", categoria=categoria, foto=imagem)
        produto_salvo = Produto.objects.get(nome="Produto Teste")
        self.assertTrue(produto_salvo.foto)

class ProdutoListagemTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Categoria Teste')
        self.produto = Produto.objects.create(
            nome='Produto Teste',
            descricao='Descrição do produto',
            preco=10.50,
            stock=100,
            validade='2025-12-31',
            categoria=self.categoria,
            destaque=True
        )

    def test_lista_produtos(self):
        response = self.client.get(reverse('lista_produtos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Produto Teste')
        self.assertContains(response, 'Descrição do produto')

class ProdutoVisualizacaoTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Categoria Teste')
        self.produto = Produto.objects.create(
            nome='Produto Teste',
            descricao='Descrição do produto',
            preco=10.50,
            stock=100,
            validade='2025-12-31',
            categoria=self.categoria,
            destaque=True
        )

    def test_ver_produto(self):
        response = self.client.get(reverse('ver_produto', kwargs={'produto_slug': self.produto.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Produto Teste')
        self.assertContains(response, 'Descrição do produto')
        self.assertContains(response, '10.50')

class ProdutoEdicaoTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Categoria Teste')
        self.produto = Produto.objects.create(
            nome='Produto Teste',
            descricao='Descrição do produto',
            preco=10.50,
            stock=100,
            validade='2025-12-31',
            categoria=self.categoria,
            destaque=True
        )

    def test_editar_produto(self):
        updated_data = {
            'nome': 'Produto Atualizado',
            'descricao': 'Descrição do produto atualizado',
            'preco': 15.00,
            'stock': 150,
            'validade': '2026-12-31',
            'categoria': self.categoria,
            'destaque': True
        }
        response = self.client.post(reverse('editar_produto', kwargs={'produto_slug': self.produto.slug}), updated_data)
        self.assertEqual(response.status_code, 302)
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, 'Produto Teste')
        self.assertEqual(self.produto.preco, 10.50)
        self.assertEqual(self.produto.stock, 100)

class ProdutoRemocaoTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Categoria Teste')
        self.produto = Produto.objects.create(
            nome='Produto Teste',
            descricao='Descrição do produto',
            preco=10.50,
            stock=100,
            validade='2025-12-31',
            categoria=self.categoria,
            destaque=True
        )

    def test_apagar_produto(self):
        response = self.client.post(reverse('apagar_produto', kwargs={'produto_slug': self.produto.slug}))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Produto.DoesNotExist):
            Produto.objects.get(id=999)

class CategoriaTests(TestCase):
    def setUp(self):
        self.categoria_data = {
            'nome': 'Nova Categoria'
        }

    def test_criar_categoria(self):
        categoria = Categoria.objects.create(nome="Nova Categoria")
        categoria_salva = Categoria.objects.get(nome="Nova Categoria")
        self.assertEqual(categoria_salva.nome, "Nova Categoria")
