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