from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from produtos.models import Produto
from .models import Carrinho, ItemCarrinho

@login_required
def adicionar_ao_carrinho(request, produto_slug):
    produto = get_object_or_404(Produto, slug=produto_slug)
    carrinho, created = Carrinho.objects.get_or_create(user=request.user)

    item_carrinho, created = ItemCarrinho.objects.get_or_create(
        carrinho=carrinho,
        produto=produto,
    )
    if not created:
        item_carrinho.quantidade += 1
        item_carrinho.save()

    messages.success(request, f'{produto.nome} foi adicionado ao seu carrinho.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def ver_carrinho(request):
    carrinho = Carrinho.objects.get(user=request.user)
    itens_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho)
    carrinho_total = 0
    total_itens = 0
    for item in itens_carrinho:
        item.preco_total = item.produto.preco * item.quantidade
        carrinho_total += item.preco_total
        total_itens += item.quantidade
    return render(request, 'ver_carrinho.html', {'itens_carrinho': itens_carrinho, 'carrinho_total': carrinho_total, 'total_itens': total_itens})