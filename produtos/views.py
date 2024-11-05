from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria
from .forms import ProdutosForm, CategoriasForm
from django.contrib import messages

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso!')
            return redirect('lista_produtos')
    else:
        form = ProdutosForm()

    return render(request, 'criar_produto.html', {'form': form})

def ver_produto(request, produto_id):
    produto = get_object_or_404(Produto, id = produto_id)
    return render(request, 'ver_produto.html', {'produto': produto})


def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutosForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('ver_produto', produto_id=produto.id)
    else:
        form = ProdutosForm(instance=produto)

    return render(request, 'editar_produto.html', {'form': form, 'produto': produto})

def apagar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto eliminado com sucesso!')
        return redirect('lista_produtos')
    return render(request, 'apagar_produto.html', {'produto': produto})



##Categorias
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria criada com sucesso!')
            return redirect('lista_categorias')
    else:
        form = CategoriasForm()

    return render(request, 'criar_categoria.html', {'form': form})

def ver_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id = categoria_id)
    return render(request, 'ver_categoria.html', {'categoria': categoria})

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id) 
    if request.method == 'POST':
        form = CategoriasForm(request.POST, instance=categoria) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso!')
            return redirect('ver_categoria', categoria_id=categoria.id) 
    else:
        form = CategoriasForm(instance=categoria)

    return render(request, 'editar_categoria.html', {'form': form, 'categoria': categoria})

def apagar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoria eliminada com sucesso!')
        return redirect('lista_categorias')
    return render(request, 'apagar_categoria.html', {'categoria': categoria})