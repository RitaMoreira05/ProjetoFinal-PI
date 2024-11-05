from django import forms
from .models import Produto

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'stock', 'foto', 'validade', 'categoria']