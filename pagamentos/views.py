from django.shortcuts import render, redirect
from django.contrib import messages
from carrinho.models import Carrinho
from encomendas.models import Encomenda, ItemEncomenda
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils.timezone import now

@login_required
def nova_compra(request):
    """
    Página onde o utilizador preenche os dados para finalizar a compra.
    """
    try:
        carrinho = Carrinho.objects.get(user=request.user)
        carrinho_total = sum(item.produto.preco * item.quantidade for item in carrinho.items.all())
    except Carrinho.DoesNotExist:
        carrinho_total = 0

    return render(request, 'nova_compra.html', {'carrinho_total': carrinho_total})

@login_required
def finalizar_compra(request):
    if request.method == 'POST':
        try:
            carrinho = Carrinho.objects.get(user=request.user) 
        except Carrinho.DoesNotExist:
            messages.error(request, "O seu carrinho está vazio.")
            return redirect('nova_compra')

        # Calcula o total do carrinho
        carrinho_total = sum(item.produto.preco * item.quantidade for item in carrinho.items.all())

        # Valida o estoque de todos os itens antes de prosseguir
        for item in carrinho.items.all():
            if item.produto.stock < item.quantidade:
                messages.error(
                    request,
                    f"O produto '{item.produto.nome}' não possui estoque suficiente. "
                    f"Estoque disponível: {item.produto.stock}, solicitado: {item.quantidade}."
                )
                return redirect('ver_carrinho')  # Redireciona para corrigir o problema

        # Captura os dados do formulário
        nome = request.POST.get('nome')
        apelido = request.POST.get('apelido')
        morada = request.POST.get('morada')
        codigo_postal = request.POST.get('cp')
        cidade = request.POST.get('cidade')

        if not morada:
            messages.error(request, "Por favor, preencha todos os campos.")
            return redirect('finalizar_compra')

        # Simula o sucesso do pagamento
        pagamento_sucesso = True
        if pagamento_sucesso:
            # Criar a encomenda
            encomenda = Encomenda.objects.create(
                user=request.user,
                data=datetime.now(),
                valor=carrinho_total,
                morada=morada,
                codigo_postal=codigo_postal,
                cidade=cidade,
            )

            # Adicionar itens da encomenda
            for item in carrinho.items.all():
                total_produto = item.produto.preco * item.quantidade
                ItemEncomenda.objects.create(
                    encomenda=encomenda,
                    produto=item.produto,
                    quantidade=item.quantidade,
                    total_produto=total_produto,
                )

            # Atualizar o estoque
            for item in carrinho.items.all():
                item.produto.stock -= item.quantidade
                item.produto.save()

            # Limpar o carrinho
            carrinho.items.all().delete()

            # Dados para a página de sucesso
            compra = {
                'valor': f"{carrinho_total:.2f} €",
                'nome_titular': f"{nome} {apelido}",
                'data': encomenda.data.strftime('%d/%m/%Y %H:%M:%S'),
            }

            messages.success(request, "Compra finalizada com sucesso!")
            return render(request, 'compra_sucesso.html', {'compra': compra})

        messages.error(request, "Houve um problema com o pagamento.")
        return redirect('nova_compra')

    return redirect('nova_compra')

@login_required
def compra_sucesso(request):
    """
    Página de sucesso da compra.
    """
    return render(request, 'compra_sucesso.html')

@login_required
def compra_falhada(request):
    """
    Página de falha da compra.
    """
    return render(request, 'compra_falhada.html')