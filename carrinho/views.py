from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from produtos.models import Produto
from .models import Carrinho, ItemCarrinho

# Função para obter o total de itens no carrinho
def obter_total_itens(user):
    try:
        carrinho = Carrinho.objects.get(user=user)
        return sum(item.quantidade for item in ItemCarrinho.objects.filter(carrinho=carrinho))
    except Carrinho.DoesNotExist:
        return 0

@login_required
def adicionar_carrinho(request, produto_slug):
    try:
        produto = Produto.objects.get(slug=produto_slug)
        
        # Verifica o estoque do produto
        if produto.stock <= 0:
            messages.error(request, f"O produto '{produto.nome}' não tem stock suficiente.")
            return redirect('ver_produto', produto_slug=produto.slug)

        # Recupera o carrinho do usuário (ou cria um novo)
        carrinho, created = Carrinho.objects.get_or_create(user=request.user)

        # Captura a quantidade informada no formulário (valor padrão 1)
        quantidade = int(request.POST.get('quantidade', 1))
        
        if quantidade < 1:
            messages.error(request, "A quantidade deve ser maior ou igual a 1.")
            return redirect('ver_produto', produto_slug=produto.slug)
        
        # Verifica se o produto já está no carrinho
        item_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho, produto=produto).first()

        if item_carrinho:
            # Se o produto já estiver no carrinho, aumenta a quantidade com o valor informado
            if item_carrinho.quantidade + quantidade <= produto.stock:  # Verifica se há estoque suficiente
                item_carrinho.quantidade += quantidade
                item_carrinho.save()
                messages.success(request, f"A quantidade de '{produto.nome}' foi aumentada no carrinho.")
            else:
                messages.error(request, f"O produto '{produto.nome}' não pode ser adicionado. Stock insuficiente.")
        else:
            # Se o produto não estiver no carrinho, cria um novo item com a quantidade informada
            if quantidade <= produto.stock:  # Verifica se há estoque suficiente para a quantidade
                ItemCarrinho.objects.create(carrinho=carrinho, produto=produto, quantidade=quantidade)
                messages.success(request, f"Produto '{produto.nome}' adicionado ao carrinho.")
            else:
                messages.error(request, f"O produto '{produto.nome}' não pode ser adicionado. Stock insuficiente.")
        
        return redirect('ver_carrinho')
    
    except Produto.DoesNotExist:
        messages.error(request, "Produto não encontrado.")
        return redirect('home')

@login_required
def ver_carrinho(request):
    try:
        # Tenta obter o carrinho do usuário
        carrinho = Carrinho.objects.get(user=request.user)
    except Carrinho.DoesNotExist:
        # Cria um novo carrinho vazio se não existir
        carrinho = Carrinho.objects.create(user=request.user)

    # Obtém os itens do carrinho
    itens_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho)

    if not itens_carrinho.exists():
        # Se o carrinho estiver vazio, exibe uma mensagem
        messages.info(request, "Seu carrinho está vazio.")
        return render(request, 'ver_carrinho.html', {
            'carrinho': carrinho,
            'itens_carrinho': [],
            'carrinho_total': 0,
            'total_itens': 0,
        })

    # Calcula os totais para um carrinho com itens
    carrinho_total = 0
    total_itens = 0
    for item in itens_carrinho:
        item.preco_total = item.produto.preco * item.quantidade
        carrinho_total += item.preco_total
        total_itens += item.quantidade

    # Renderiza a página com os detalhes do carrinho
    return render(request, 'ver_carrinho.html', {
        'carrinho': carrinho,
        'itens_carrinho': itens_carrinho,
        'carrinho_total': carrinho_total,
        'total_itens': total_itens,
    })

@login_required
def remover_do_carrinho(request, produto_slug):
    carrinho = get_object_or_404(Carrinho, user=request.user)
    item = get_object_or_404(ItemCarrinho, carrinho=carrinho, produto__slug=produto_slug)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item removido do carrinho com sucesso.')
    return redirect('ver_carrinho')

@login_required
def atualizar_quantidade(request, produto_slug):
    carrinho = get_object_or_404(Carrinho, user=request.user)
    item = get_object_or_404(ItemCarrinho, carrinho=carrinho, produto__slug=produto_slug)
    if request.method == 'POST':
        nova_quantidade = int(request.POST.get('quantidade', 1))
        if nova_quantidade > 0:
            item.quantidade = nova_quantidade
            item.save()
            messages.success(request, 'Quantidade atualizada com sucesso.')
        else:
            messages.error(request, 'A quantidade deve ser maior que zero.')
    return redirect('ver_carrinho')
