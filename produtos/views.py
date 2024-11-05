from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutosForm

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutosForm()

    return render(request, 'criar_produto.html', {'form': form})

