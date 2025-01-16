from django.shortcuts import render, redirect
from .forms import CompraForm
from django.contrib import messages
from carrinho.models import Carrinho, ItemCarrinho
from django.shortcuts import get_object_or_404

def nova_compra(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compra_sucesso')  # Redireciona para uma página de sucesso
    else:
        form = CompraForm()
    return render(request, 'nova_compra.html', {'form': form})

def compra_pendente(compra):
    # Simule o processamento do pagamento
    # Retorne 'sucesso', 'pendente' ou 'falha' com base na lógica do pagamento
    return 'sucesso'  # Exemplo de retorno

def finalizar_compra(request):
    carrinho = get_object_or_404(Carrinho, user=request.user)
    itens_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho)
    carrinho_total = 0
    for item in itens_carrinho:
        carrinho_total += item.produto.preco * item.quantidade

    if request.method == 'POST':
        # Aqui você pode processar os dados do formulário personalizado
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        cidade = request.POST.get('cidade')
        distrito = request.POST.get('distrito')
        cp = request.POST.get('cp')
        cartao = request.POST.get('cartao')
        validade = request.POST.get('validade')
        cvv = request.POST.get('cvv')

        # Verifique se todos os campos estão preenchidos
        if None in [nome, endereco, cidade, distrito, cp, cartao, validade, cvv]:
            messages.error(request, "Por favor, preencha todos os campos.")
            return render(request, 'nova_compra.html', {'carrinho_total': carrinho_total})

        # Simule o processamento do pagamento
        status = compra_pendente(None)  # Função fictícia
        if status == 'sucesso':
            return redirect('compra_sucesso')
        else:
            return redirect('compra_falhada')
    return render(request, 'nova_compra.html', {'carrinho_total': carrinho_total})