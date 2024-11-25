from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria
from .forms import ProdutosForm, CategoriasForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

def home(request):
    # Busca produtos marcados como destaque
    produtos_destaque = Produto.objects.filter(em_destaque=True)[:5]  # Ajusta o número conforme necessário
    return render(request, 'home.html', {'produtos_destaque': produtos_destaque})

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

@staff_member_required
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso!')
            return redirect('produtos/lista_produtos')
    else:
        form = ProdutosForm()

    return render(request, 'produtos/criar_produto.html', {'form': form})

def ver_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    origem = request.GET.get('origem', 'produtos')
    categoria_id = request.GET.get('categoria_id')
    return render(request, 'produtos/ver_produto.html', {
        'produto': produto,
        'origem': origem,
        'categoria_id': categoria_id
    })

@staff_member_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutosForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('produtos/ver_produto', produto_id=produto.id)
    else:
        form = ProdutosForm(instance=produto)

    return render(request, 'produtos/editar_produto.html', {'form': form, 'produto': produto})

@staff_member_required
def apagar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto eliminado com sucesso!')
        return redirect('produtos/lista_produtos')
    return render(request, 'produtos/apagar_produto.html', {'produto': produto})



#Categorias
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'produtos/lista_categorias.html', {'categorias': categorias})

@staff_member_required
def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria criada com sucesso!')
            return redirect('produtos/lista_categorias')
    else:
        form = CategoriasForm()

    return render(request, 'produtos/criar_categoria.html', {'form': form})

def ver_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id = categoria_id)
    produtos = categoria.produtos.all()  # usa o related_name definido
    return render(request, 'produtos/ver_categoria.html', {'categoria': categoria, 'produtos': produtos})

@staff_member_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id) 
    if request.method == 'POST':
        form = CategoriasForm(request.POST, instance=categoria) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso!')
            return redirect('produtos/ver_categoria', categoria_id=categoria.id) 
    else:
        form = CategoriasForm(instance=categoria)

    return render(request, 'produtos/editar_categoria.html', {'form': form, 'categoria': categoria})

@staff_member_required
def apagar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoria eliminada com sucesso!')
        return redirect('produtos/lista_categorias')
    return render(request, 'produtos/apagar_categoria.html', {'categoria': categoria})