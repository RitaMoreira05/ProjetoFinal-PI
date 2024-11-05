from django import forms
from .models import Produto, Categoria

class ProdutosForm(forms.ModelForm):
    validade = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'stock', 'foto', 'validade', 'categoria']

class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'slug']