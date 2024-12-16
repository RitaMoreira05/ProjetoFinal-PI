from django import forms
from .models import Produto, Categoria

class ProdutosForm(forms.ModelForm):
    """
    Formulário para criar e editar produtos.

    Campos:
        validade (DateField): A data de validade do produto, exibida com um widget de entrada de data.
    """
    validade = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        """
        Metadados para o formulário de produtos.

        Atributos:
            model (Produto): O modelo associado a este formulário.
            fields (list): A lista de campos a serem exibidos no formulário.
        """
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'stock', 'foto', 'validade', 'categoria', 'destaque']

class CategoriasForm(forms.ModelForm):
    """
    Formulário para criar e editar categorias.

    Metadados:
        model (Categoria): O modelo associado a este formulário.
        fields (list): A lista de campos a serem exibidos no formulário.
    """
    class Meta:
        """
        Metadados para o formulário de categorias.

        Atributos:
            model (Categoria): O modelo associado a este formulário.
            fields (list): A lista de campos a serem exibidos no formulário.
        """
        model = Categoria
        fields = ['nome']
	